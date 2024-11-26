import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.3 or intoxication > 0.1 or time_since_slept >= 8:
        return 3  # Sleep
    if 0.3 <= alertness < 0.7 and hypertension < 0.02:
        return 1  # Drink coffee and work
    if 0.7 <= alertness or (time_since_slept < 6 and hypertension < 0.015):
        return 0  # Just work
    return 2  # Drink beer and work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)