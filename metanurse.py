import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension >= 0.02 or intoxication >= 0.02:
        return 3

    if time_since_slept > 2.5:
        return 3

    if alertness < 0.75:
        if hypertension < 0.015:
            return 1
        return 3

    if alertness >= 0.85 and intoxication < 0.01:
        return 0

    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)