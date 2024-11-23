import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.65 or intoxication > 0.35:
        return 3
    if time_since_slept > 10:
        return 3
    if alertness < 0.3:
        return 3 if time_elapsed >= 4 else 1
    if time_since_slept > 8:
        return 3
    if work_done < 0.4 and alertness > 0.6:
        return 0
    if time_since_slept > 4 and alertness < 0.6:
        return 1
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)