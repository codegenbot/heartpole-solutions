import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness <= 0.2 or hypertension >= 0.7 or intoxication >= 0.7 or time_since_slept >= 8:
        return 3  # Sleep to recover
    if alertness > 0.7 and hypertension < 0.5 and intoxication < 0.5:
        return 0  # Just work
    if 0.4 < alertness <= 0.7 and hypertension < 0.5 and intoxication < 0.5:
        return 1  # Drink coffee and work
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)