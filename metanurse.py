import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Ensure sleep if absolutely necessary considering both alertness and rest
    if alertness < 0.5 or time_since_slept >= 6:
        return 3  # Sleep to recover

    # Use coffee moderately given alertness while keeping hypertension in check
    if alertness < 0.65 and hypertension < 0.05:
        return 1  # Coffee to boost alertness

    # Ensure very good conditions for beer to minimize risk
    if alertness > 0.9 and intoxication < 0.01 and hypertension < 0.004:
        return 2  # Reward with beer under optimal conditions

    return 0  # Default to work if conditions are stable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)