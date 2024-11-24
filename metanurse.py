import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if any serious health alert is present
    if (
        alertness < 0.6
        or time_since_slept > 4
        or hypertension > 0.6
        or intoxication > 0.5
    ):
        return 3
    # Drink coffee if alertness is moderate, but avoid if it risks hypertension
    if alertness < 0.8 and hypertension < 0.5:
        return 1
    # Work normally if all indicators are within healthy ranges
    if alertness >= 0.8 and hypertension < 0.4 and intoxication < 0.3:
        return 0
    # Return 0 by default if all specific conditions are not met
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)