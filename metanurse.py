import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.6 or time_since_slept > 8:
        return 3
    elif hypertension >= 0.5:
        return 3
    elif intoxication >= 0.35:
        return 3
    elif 0.2 <= intoxication < 0.35 and alertness > 0.75:
        return 2
    elif alertness < 0.75 and hypertension <= 0.35 and intoxication < 0.2:
        return 1
    else:
        return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)