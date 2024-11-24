import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness <= 0.3 or hypertension >= 0.7 or intoxication >= 0.7 or time_since_slept > 6:
        return 3
    if alertness > 0.9 and hypertension < 0.4 and intoxication < 0.4:
        return 0
    if 0.3 < alertness <= 0.9 and hypertension < 0.4 and intoxication < 0.4:
        return 1
    if 0.3 < alertness <= 0.6 and hypertension < 0.4 and intoxication < 0.6:
        return 2
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)