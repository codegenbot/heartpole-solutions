import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        alertness < 0.4
        or hypertension > 0.8
        or intoxication > 0.5
        or time_since_slept > 10
    ):
        return 3
    if alertness >= 0.7 and hypertension < 0.6 and intoxication < 0.2:
        return 0
    if (
        alertness < 0.7
        and hypertension < 0.65
        and intoxication < 0.25
        and time_since_slept <= 10
    ):
        return 1
    if hypertension < 0.7 and 0.25 <= intoxication < 0.45:
        return 2
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)