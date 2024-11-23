import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 8 or hypertension > 0.7 or intoxication > 0.5:
        return 3
    if alertness < 0.5 and hypertension < 0.5 and intoxication <= 0.3:
        return 1
    if intoxication > 0.2 and alertness > 0.6:
        return 0
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)