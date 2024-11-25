import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept >= 4 or alertness < 0.4 or intoxication > 0.08:
        return 3
    if 0.4 <= alertness < 0.6 and hypertension < 0.02:
        return 1
    if alertness >= 0.6 and hypertension < 0.02 and intoxication < 0.02:
        return 0
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)