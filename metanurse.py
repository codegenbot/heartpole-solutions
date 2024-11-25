import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.01 or intoxication > 0.015:
        return 3
    if alertness < 0.7 or time_since_slept > 6:
        return 3
    if 0.7 <= alertness < 0.85 and hypertension < 0.01 and intoxication < 0.01:
        return 1
    if intoxication < 0.005 and time_elapsed > 20 and work_done < 3:
        return 2
    if alertness >= 0.85:
        return 0
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)