import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        alertness < 0.3
        or hypertension > 0.15
        or intoxication > 0.20
        or time_since_slept > 8
    ):
        return 3  # Sleep
    if alertness < 0.5 or time_since_slept > 6:
        return 3  # Sleep
    if alertness < 0.7 and hypertension < 0.10:
        return 1  # Drink coffee and work
    return 0  # Just work


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)