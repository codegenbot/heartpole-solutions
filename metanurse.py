import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        alertness < 0.4
        or time_since_slept >= 6
        or intoxication > 0.1
        or hypertension > 0.06
    ):
        return 3

    if (0.05 < hypertension <= 0.06) or (0.05 < intoxication <= 0.1):
        return 3

    if alertness < 0.6 and hypertension <= 0.02 and intoxication <= 0.02:
        return 1

    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)