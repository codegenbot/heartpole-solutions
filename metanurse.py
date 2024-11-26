import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept >= 6 or alertness < 0.4:
        return 3
    if hypertension > 0.02 or intoxication > 0.1:
        return 3
    if 0.4 <= alertness < 0.65 and time_since_slept < 4:
        return 1
    if 0.65 <= alertness < 0.75 and hypertension < 0.005:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)