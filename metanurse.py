import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension >= 0.05 or intoxication >= 0.15:
        return 3
    if alertness < 0.3 or time_since_slept >= 8:
        return 3
    if 0.3 <= alertness < 0.6:
        if hypertension < 0.02:
            return 1
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)