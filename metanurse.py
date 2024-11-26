import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.01 or intoxication > 0.03:
        return 3
    if time_since_slept > 4 or alertness < 0.6:
        return 3
    if 0.6 <= alertness < 0.8 and hypertension < 0.008 and intoxication < 0.018:
        return 1
    if 0.8 <= alertness < 0.9 and hypertension < 0.005 and intoxication < 0.009:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)