import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.5 or time_since_slept >= 6:
        return 3
    if hypertension >= 0.03:
        return 3 if time_since_slept < 6 else 2
    if intoxication >= 0.12:
        return 3 if time_since_slept >= 5 else 2
    if 0.7 <= alertness < 0.9 and hypertension < 0.025 and intoxication < 0.08:
        return 1
    if alertness >= 0.9 and hypertension < 0.025 and intoxication < 0.08 and time_since_slept < 5:
        return 0
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)