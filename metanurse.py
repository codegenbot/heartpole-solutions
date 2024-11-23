import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediately sleep if alertness is very low or if sleep deprivation is high
    if alertness < 0.3 or time_since_slept > 8:
        return 3

    # Use coffee if alertness is medium-low and health risks are negligible
    if alertness < 0.6 and hypertension < 0.2 and intoxication < 0.1:
        return 1

    # Avoid beer unless intoxication is negligible and alertness is very low
    if alertness < 0.4 and intoxication < 0.05:
        return 2

    # Work if conditions are moderate or better
    if alertness > 0.5 and hypertension < 0.2 and intoxication < 0.1:
        return 0

    # Default to working if there's no immediate health trigger
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)