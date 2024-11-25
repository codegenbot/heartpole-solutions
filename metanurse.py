import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.2 or hypertension > 0.9 or intoxication > 0.7:
        return 3
    if alertness > 0.9 and hypertension < 0.6 and intoxication < 0.2:
        return 0
    if 0.3 <= alertness <= 0.8 and hypertension < 0.7 and intoxication < 0.3:
        return 1
    if alertness < 0.3 and hypertension < 0.6 and intoxication < 0.3:
        return 2
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)