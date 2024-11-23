import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.35 or intoxication > 0.25:
        return 3
    if time_since_slept > 10 or alertness < 0.25:
        return 3
    if alertness < 0.5 and time_elapsed < 7:
        return 1
    if (
        intoxication <= 0.15
        and alertness < 0.5
        and work_done < 0.5
        and time_elapsed < 9
    ):
        return 2
    if (
        alertness >= 0.35
        and hypertension <= 0.15
        and intoxication <= 0.15
        and work_done < 0.8
    ):
        return 0
    if alertness < 0.35 and time_elapsed > 9:
        return 3
    return 0 if alertness >= 0.4 else 3


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)