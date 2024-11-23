import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.2 or time_since_slept >= 7:
        return 3
    if alertness < 0.5 and hypertension < 0.12:
        return 1
    if alertness >= 0.6 and hypertension <= 0.1 and intoxication <= 0.03:
        return 0
    if intoxication < 0.03:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)