import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 20 or alertness < 0.3 or hypertension > 0.8 or intoxication > 0.6:
        return 3
    if alertness >= 0.7 and hypertension < 0.5 and intoxication < 0.3:
        return 0
    if 0.45 <= alertness < 0.7 and hypertension < 0.65 and intoxication < 0.45:
        return 1
    if time_since_slept > 12 or alertness < 0.4 or hypertension > 0.7 or intoxication > 0.5:
        return 3
    return 1

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)