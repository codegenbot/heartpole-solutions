import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.02 or intoxication > 0.08:
        return 3
    if alertness < 0.5 or time_since_slept > 6:
        return 3
    if alertness < 0.7 and hypertension < 0.01:
        return 1
    if alertness >= 0.9 and intoxication <= 0.05:
        return 2
    if work_done > 60:
        return 3
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)