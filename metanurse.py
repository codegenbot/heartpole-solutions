import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if alertness is low or too long since last slept
    if alertness < 0.6 or time_since_slept > 7:
        return 3

    # Avoid caffeine and sleep if hypertension is higher
    if hypertension >= 0.06:
        return 3 if alertness < 0.7 else 0

    # Avoid work if intoxication is significant
    if intoxication >= 0.08:
        return 3

    # Use coffee to boost productivity if safe
    if 0.6 <= alertness < 0.75 and hypertension < 0.04 and intoxication < 0.05:
        return 1

    # Optimal state for productive work
    if alertness >= 0.75:
        return 0

    # Default to work if conditions don't require sleep or caffeine avoidance
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)