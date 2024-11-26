import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.01 or intoxication > 0.1:
        return 3
    if time_since_slept >= 6:
        return 3
    if alertness < 0.5:
        return 3
    if alertness < 0.7 and hypertension < 0.007 and intoxication < 0.05:
        return 1
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)