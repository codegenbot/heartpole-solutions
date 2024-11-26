import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.6 or hypertension >= 0.018 or intoxication > 0.08 or time_since_slept >= 7:
        return 3
    if alertness < 0.75 and hypertension < 0.012 and time_since_slept < 6:
        return 1
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)