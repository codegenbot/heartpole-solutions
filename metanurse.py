import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.5 or hypertension >= 0.02 or intoxication > 0.1 or time_since_slept >= 7:
        return 3
    if 0.5 <= alertness < 0.65 and hypertension < 0.015:
        return 1
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)