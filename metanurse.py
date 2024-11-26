import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept >= 5 or alertness < 0.5:
        return 3
    if hypertension > 0.015 or intoxication > 0.08:
        return 3
    if 0.5 <= alertness < 0.7 and time_since_slept < 3:
        return 1
    if 0.7 <= alertness < 0.8 and hypertension < 0.004 and intoxication < 0.05:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)