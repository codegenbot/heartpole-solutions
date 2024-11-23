import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.6 or intoxication > 0.4:
        return 3
    if alertness < 0.35 or time_since_slept > 10:
        return 3
    if alertness < 0.65 and hypertension < 0.35:
        return 1
    if alertness >= 0.55 and hypertension <= 0.3 and intoxication <= 0.25:
        return 0
    if time_elapsed >= 14:
        return 3
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)