import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.25 or intoxication > 0.2 or time_since_slept > 8:
        return 3
    if alertness < 0.4 or time_since_slept >= 6:
        return 3
    if 0.4 <= alertness < 0.6 and hypertension < 0.15 and intoxication < 0.1:
        return 1
    if 0.6 <= alertness < 0.8 and intoxication < 0.05:
        return 0
    if 0.55 <= alertness < 0.75 and intoxication < 0.1:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)