import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.5 or intoxication > 0.5:
        return 3

    if alertness < 0.4:
        return 3

    if time_since_slept > 8:
        return 3

    if alertness < 0.6:
        if hypertension < 0.4 and intoxication < 0.3:
            return 1
        else:
            return 3

    if alertness >= 0.7 and hypertension < 0.4:
        return 0

    return 1


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)