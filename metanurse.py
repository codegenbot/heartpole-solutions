import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept >= 8 or alertness < 0.2:
        return 3

    if hypertension > 0.85:
        return 3 if intoxication > 0.15 else 2 

    if alertness < 0.7 and hypertension < 0.5 and intoxication < 0.15:
        return 1

    if alertness >= 0.8 and hypertension <= 0.3 and intoxication <= 0.1:
        return 0

    if 0.5 <= alertness < 0.8 and hypertension < 0.6:
        return 0

    if hypertension > 0.6 and intoxication < 0.2:
        return 2

    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)