import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.4 or hypertension > 0.6 or intoxication > 0.4 or time_since_slept > 6:
        return 3  # Sleep to recover

    if alertness > 0.9 and hypertension < 0.5 and intoxication < 0.2:
        return 0  # Just work

    if 0.6 <= alertness <= 0.9 and hypertension < 0.55 and intoxication < 0.3:
        return 1  # Drink coffee and work

    if 0.5 <= alertness < 0.6 and intoxication < 0.15:
        return 2  # Drink beer and work

    return 3  # Default to sleep for safety

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)