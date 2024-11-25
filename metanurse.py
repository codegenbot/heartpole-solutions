import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep to reduce health risks if necessary
    if (
        alertness < 0.4
        or hypertension > 0.09
        or intoxication > 0.08
        or time_since_slept >= 8
    ):
        return 3

    # Allow coffee to boost alertness if conditions permit
    if 0.4 <= alertness < 0.65 and hypertension < 0.05 and intoxication < 0.04:
        return 1

    # Prefer work to maximize productivity within healthy limits
    if alertness >= 0.65 and hypertension < 0.07 and intoxication < 0.06:
        return 0

    # Revert to beer and work for last resort relaxation if needed
    if intoxication < 0.05:
        return 2

    # Default to work if no other conditions are met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)