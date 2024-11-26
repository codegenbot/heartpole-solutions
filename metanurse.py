import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if any serious threshold is reached
    if (
        alertness < 0.5
        or hypertension >= 0.015  # Lowered threshold
        or intoxication > 0.1
        or time_since_slept >= 6
    ):
        return 3
    # Use coffee if alertness is low, and hypertension is safe
    if 0.5 <= alertness < 0.7 and hypertension < 0.012:  # Updated alertness range
        return 1
    # Avoid beer if intoxication could rise quickly
    if 0.7 <= alertness < 0.8 and hypertension < 0.01 and intoxication < 0.03:  # Lower intoxication threshold
        return 2
    # Continue working if conditions are optimal
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)