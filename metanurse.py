import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if low alertness or long time since sleep
    if alertness < 0.7 or time_since_slept > 8:
        return 3

    # Avoid excessive work if intoxication or significant hypertension is present
    if intoxication >= 0.1 or hypertension >= 0.08:
        return 3

    # Use caffeine sparingly if alertness is low, and no hypertension issues
    if alertness < 0.75 and hypertension < 0.04:
        return 1

    # Optimal conditions for productive work
    if alertness >= 0.8:
        return 0

    # Default to reduced workload strategy if conditions are not optimal
    return 2 if alertness < 0.7 else 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)