import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.65 or intoxication > 0.45:
        return 3
    if time_since_slept > 12 or alertness < 0.3:
        return 3
    if time_elapsed < 10 and alertness < 0.7 and hypertension < 0.4:
        return 1
    if alertness >= 0.5 and hypertension <= 0.3 and intoxication <= 0.2:
        return 0
    if time_elapsed >= 14 or alertness < 0.4:
        return 3
    return 0 

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)