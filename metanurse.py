import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep more aggressively
    if alertness < 0.5 or hypertension > 0.7 or intoxication > 0.5 or time_since_slept > 7:
        return 3  # Sleep to recover

    if alertness > 0.85 and hypertension < 0.5 and intoxication < 0.2:
        return 0  # Just work

    if 0.65 <= alertness <= 0.85 and hypertension < 0.55 and intoxication < 0.25:
        return 1  # Drink coffee and work

    if 0.6 <= alertness < 0.65 and intoxication < 0.15:
        return 2  # Drink beer and work

    return 3  # Default to sleep for safety

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)