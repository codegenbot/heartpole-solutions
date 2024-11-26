import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.5 or hypertension >= 0.03 or intoxication > 0.15 or time_since_slept >= 7:
        return 3
    if 0.5 <= alertness < 0.8 and hypertension < 0.02 and intoxication < 0.1:
        return 1
    if alertness >= 0.8 and hypertension < 0.02 and intoxication < 0.1 and time_since_slept < 6:
        return 0
    if intoxication >= 0.1:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)