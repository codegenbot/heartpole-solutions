import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.7 or intoxication > 0.5:
        return 3
    if time_since_slept > 14:
        return 3
    if alertness < 0.3 and time_elapsed < 8 and time_since_slept < 12:
        return 1
    if alertness < 0.4 and time_since_slept >= 12:
        return 3
    if work_done < 0.5 and alertness > 0.5:
        return 0
    if alertness < 0.7 and time_elapsed < 10:
        return 1
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)