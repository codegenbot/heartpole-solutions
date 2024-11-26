import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.03 or intoxication > 0.04:
        return 3
    if time_since_slept > 6:
        return 3

    if alertness < 0.7:
        if hypertension < 0.02 and intoxication < 0.02:
            return 1

    if alertness > 0.75 and hypertension < 0.015 and intoxication < 0.015:
        return 0

    if work_done > 25 or time_elapsed > 60:
        return 3

    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)