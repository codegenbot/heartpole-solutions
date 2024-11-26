import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if any critical or near-critical threshold is crossed
    if (
        alertness < 0.6
        or time_since_slept >= 5
        or intoxication >= 0.05
        or hypertension > 0.07
    ):
        return 3  # Sleep to recover

    # Drink coffee if alertness is low and it's safe for blood pressure
    if alertness < 0.75 and hypertension < 0.04:
        return 1  # Coffee to boost alertness moderately

    # Avoid beer consumption as this seemed non-beneficial
    return 0  # Default to work when conditions are generally stable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)