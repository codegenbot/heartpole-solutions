import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        time_since_slept > 15
        or alertness < 0.25
        or hypertension > 0.8
        or intoxication > 0.7
    ):
        return 3  # Sleep

    if alertness > 0.75 and hypertension < 0.35 and intoxication < 0.15:
        return 0  # Just Work

    if alertness < 0.5 and hypertension < 0.6 and time_since_slept > 5:
        return 1  # Drink coffee and work

    if alertness < 0.55 and intoxication < 0.3 and hypertension < 0.6:
        return 2  # Drink beer and work

    return 3  # Default action


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)