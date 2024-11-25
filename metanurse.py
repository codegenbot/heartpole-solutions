import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if alertness is low or very long since last slept
    if alertness < 0.5 or time_since_slept > 8:
        return 3

    # Avoid caffeine if high hypertension
    if hypertension >= 0.07:
        return 3 if alertness < 0.6 else 0

    # Avoid work if intoxication is too high
    if intoxication >= 0.1:
        return 3

    # Use coffee to boost productivity if safe
    if 0.5 <= alertness < 0.7 and hypertension < 0.05:
        return 1

    # Optimal state for productive work
    if alertness >= 0.7:
        return 0

    # Default to work if conditions don't require sleep or caffeine avoidance
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)