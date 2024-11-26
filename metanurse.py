import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.015 or intoxication > 0.025:
        return 3
    if time_since_slept > 4:
        return 3

    if alertness < 0.8:
        if hypertension < 0.015 and intoxication < 0.015 and time_since_slept < 3:
            return 1

    if alertness >= 0.8 and hypertension < 0.01 and intoxication < 0.01:
        return 0

    if work_done > 10 and time_elapsed > 25:
        return 3

    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)