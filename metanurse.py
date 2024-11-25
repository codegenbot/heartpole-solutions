def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if alertness is low, or significant time since last sleep, or hypertension is high
    if (
        alertness < 0.25
        or time_since_slept >= 4
        or hypertension > 0.1
        or intoxication > 0.08
    ):
        return 3

    # Drink coffee if alertness is low, avoiding hypertension and intoxication
    if 0.25 <= alertness < 0.5 and hypertension < 0.04 and intoxication < 0.03:
        return 1

    # Continue working if alertness is sufficient, and health indicators are stable
    if alertness >= 0.5 and hypertension < 0.02 and intoxication < 0.01:
        return 0

    # Default to work if no immediate critical health flags
    return 0


import sys

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)