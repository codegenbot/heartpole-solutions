import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.2 or intoxication > 0.25 or time_since_slept >= 8:
        return 3
    if alertness < 0.5 and hypertension < 0.1:
        return 1
    if alertness >= 0.8 and hypertension < 0.05 and intoxication < 0.02:
        return 0
    if intoxication < 0.1:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)