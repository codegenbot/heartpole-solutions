import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.3 or time_since_slept >= 8:
        return 3
    if time_since_slept > 6 and alertness < 0.5:
        return 3
    if alertness < 0.5 and hypertension < 0.15:
        return 1
    if alertness < 0.4 and intoxication < 0.05 and time_since_slept <= 5:
        return 2
    if alertness >= 0.7 and hypertension <= 0.1 and intoxication <= 0.05:
        return 0
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)