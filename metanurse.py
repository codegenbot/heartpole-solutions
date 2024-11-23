import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.6 or intoxication > 0.4 or alertness < 0.2 or time_since_slept > 14:
        return 3
    if alertness < 0.35:
        return 3
    if alertness >= 0.7 and hypertension <= 0.2 and intoxication <= 0.05:
        return 0
    if 0.4 <= alertness < 0.7 and hypertension <= 0.35 and intoxication < 0.05:
        return 1
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)