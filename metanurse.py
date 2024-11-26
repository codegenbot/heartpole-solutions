import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.02 or intoxication > 0.1:
        return 3
    if time_since_slept >= 8:
        return 3
    if alertness < 0.4:
        return 3
    if alertness < 0.5 and hypertension < 0.01:
        return 1
    if 0.5 <= alertness < 0.65 and hypertension < 0.01:
        return 1
    if 0.65 <= alertness < 0.85 and hypertension < 0.01 and intoxication < 0.05:
        return 0
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)