import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.02 or intoxication > 0.02:
        return 3
    if alertness < 0.4 or time_since_slept > 5:
        return 3
    if 0.3 <= alertness < 0.7 and hypertension < 0.02 and time_elapsed < 12:
        return 1
    if intoxication == 0 and hypertension < 0.02 and time_elapsed > 12:
        return 2
    if alertness >= 0.7:
        return 0
    return 1

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)