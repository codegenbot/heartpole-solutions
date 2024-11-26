import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Priority to prevent severe conditions
    if hypertension > 0.04 or intoxication > 0.05:
        return 3

    # Consider sleep if significantly overdue
    if time_since_slept > 8:
        return 3

    # Encourage coffee use more
    if alertness < 0.6:
        if hypertension < 0.03 and intoxication < 0.03:
            return 1

    # Encourage work when safe
    if alertness > 0.5 and hypertension < 0.03 and intoxication < 0.03:
        return 0

    # Guard against exhaustion
    if work_done > 20 and time_elapsed > 50:
        return 3

    # Default to general productivity
    if alertness >= 0.6:
        return 0

    # Default: Sleep
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)