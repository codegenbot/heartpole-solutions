import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.6 or time_since_slept > 6:
        return 3  # Sleep
    if alertness >= 0.8 and hypertension < 0.3 and intoxication < 0.1:
        return 0  # Just work
    if 0.6 <= alertness < 0.8 and hypertension < 0.4 and intoxication < 0.1:
        return 1  # Drink coffee and work
    if intoxication < 0.05 and hypertension < 0.3:
        return 2  # Drink beer and work
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)