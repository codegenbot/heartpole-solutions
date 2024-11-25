import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.5 or time_since_slept > 5 or hypertension > 0.4:
        return 3  # Sleep

    if 0.6 <= alertness <= 1.0 and hypertension <= 0.25 and intoxication < 0.01:
        return 0  # Just work

    if 0.5 <= alertness < 0.6 and hypertension < 0.4 and intoxication < 0.02:
        return 1  # Drink coffee and work

    if 0.45 <= alertness < 0.5 and intoxication == 0.0 and hypertension < 0.3:
        return 2  # Drink beer and work

    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)