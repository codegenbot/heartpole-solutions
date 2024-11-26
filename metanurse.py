import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        alertness < 0.4
        or hypertension >= 0.03
        or intoxication > 0.15
        or time_since_slept >= 7
    ):
        return 3
    if (
        0.4 <= alertness < 0.7
        and hypertension < 0.02
        and intoxication < 0.1
        and time_since_slept < 5
    ):
        return 1
    if alertness >= 0.7 and hypertension < 0.02 and intoxication < 0.1:
        return 0
    if intoxication >= 0.1 and hypertension < 0.025:
        return 2
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)