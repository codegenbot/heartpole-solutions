import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept >= 8 or alertness < 0.3:
        return 3
    if hypertension > 0.03 or intoxication > 0.15:
        return 3
    if 0.3 <= alertness < 0.6 and time_since_slept < 6:
        return 1
    if 0.6 <= alertness < 0.8 and hypertension < 0.01 and intoxication < 0.05:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)