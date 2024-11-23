import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.5 or hypertension > 0.55 or intoxication > 0.4 or time_since_slept >= 8:
        return 3
    if alertness < 0.6 and hypertension < 0.5:
        return 1
    if 0.4 < hypertension <= 0.6 and intoxication < 0.2:
        return 2
    if alertness >= 0.6 and hypertension < 0.4 and intoxication < 0.15:
        return 0
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)