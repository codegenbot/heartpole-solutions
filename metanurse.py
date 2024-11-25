import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.4 or time_since_slept > 6 or hypertension > 0.6:
        return 3
    if alertness > 0.8 and hypertension < 0.2 and intoxication == 0.0:
        return 0
    if 0.5 <= alertness <= 0.8 and hypertension < 0.4:
        return 1
    if alertness < 0.5 and intoxication < 0.2 and hypertension < 0.3:
        return 2
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)