import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 5 or hypertension > 0.3 or intoxication > 0.2:
        return 3
    if alertness < 0.6 and hypertension < 0.15:
        return 1
    if alertness >= 0.75 and hypertension < 0.1:
        return 0
    return 2 if intoxication < 0.15 else 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)