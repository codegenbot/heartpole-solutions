import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if any serious threshold is reached
    if (
        alertness < 0.5
        or hypertension >= 0.012  # Further lowered threshold
        or intoxication > 0.05  # Lower limit
        or time_since_slept >= 5  # Encourage more frequent sleep
    ):
        return 3
    # Use coffee if alertness is low, and hypertension is safe
    if 0.5 <= alertness < 0.8 and hypertension < 0.01:  # Expanded alertness range
        return 1
    # Continue working if alertness is optimal
    if alertness >= 0.8 and hypertension < 0.01 and intoxication < 0.02:
        return 0
    # Avoid beer if intoxication could rise quickly
    if alertness >= 0.7 and hypertension < 0.009 and intoxication < 0.02:  # Adjusted for lower risk
        return 2
    # Default to work
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)