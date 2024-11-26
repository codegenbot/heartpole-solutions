import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.03:
        return 3
    if intoxication > 0.12:
        return 3

    if alertness < 0.25:
        return 3

    if time_since_slept > 10:
        return 3

    if alertness < 0.6 and hypertension < 0.03 and work_done < 80:
        return 1

    if alertness >= 0.5:
        return 0

    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)