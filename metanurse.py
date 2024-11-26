import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        alertness < 0.65
        or time_since_slept > 3
        or intoxication > 0.08
        or hypertension > 0.03
    ):
        return 3
    if alertness < 0.8 and hypertension < 0.04 and time_since_slept < 3:
        return 1
    if 0.8 <= alertness < 0.9 and intoxication < 0.05 and hypertension < 0.02:
        return 2
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)