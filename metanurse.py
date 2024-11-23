import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 8 or hypertension > 0.4 or intoxication > 0.4:
        return 3
    if work_done > 20 and intoxication < 0.2 and hypertension < 0.3:
        return 2
    if alertness < 0.5 and hypertension < 0.35:
        return 1
    if alertness > 0.7 and hypertension < 0.25 and intoxication < 0.15:
        return 0
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)