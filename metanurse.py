import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.35 or intoxication > 0.35 or time_since_slept > 4:
        return 3
    if alertness < 0.6:
        if hypertension < 0.2 and intoxication < 0.15:
            return 1
        else:
            return 3
    if alertness >= 0.8:
        return 0
    if work_done > 10 and alertness > 0.5:
        return 0
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)