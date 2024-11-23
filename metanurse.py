import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.6 or intoxication > 0.4:
        return 3

    if time_since_slept > 15 or (alertness < 0.4 and time_elapsed >= 14):
        return 3

    if alertness < 0.5:
        if time_elapsed < 9:
            return 1

    if alertness >= 0.5 and work_done < 0.8:
        return 0

    return 3 if alertness < 0.6 else 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)