import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.55 or intoxication > 0.35:
        return 3
    if time_since_slept > 14 or alertness < 0.3:
        return 3
    if alertness < 0.7 and hypertension < 0.35:
        return 1
    if alertness > 0.6 and hypertension <= 0.4 and intoxication <= 0.25:
        return 0
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)