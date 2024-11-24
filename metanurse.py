import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 6 or hypertension >= 0.3 or intoxication >= 0.3:
        return 3
    if alertness >= 0.85 and hypertension < 0.15 and intoxication < 0.15:
        return 0
    if alertness < 0.7 and hypertension < 0.25:
        return 1
    return 2

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)