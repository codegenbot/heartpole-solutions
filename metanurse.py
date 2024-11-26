import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.4 or hypertension >= 0.02 or intoxication > 0.1 or time_since_slept >= 6:
        return 3
    if 0.4 <= alertness < 0.6 and hypertension < 0.015:
        return 1
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)