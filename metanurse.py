import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.5 or hypertension > 0.55 or intoxication > 0.25:
        return 3
    if time_since_slept >= 4:
        return 3
    if alertness < 0.65 and hypertension <= 0.5 and intoxication <= 0.2:
        return 1
    if alertness >= 0.75 and hypertension <= 0.4 and intoxication <= 0.1:
        return 0
    if alertness >= 0.7 and hypertension < 0.45 and intoxication <= 0.2:
        return 2
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)