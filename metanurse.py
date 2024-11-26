import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if any critical threshold is crossed
    if (
        alertness < 0.4
        or time_since_slept >= 6
        or intoxication > 0.12
        or hypertension > 0.08
    ):
        return 3  # Sleep to recover

    # Drink coffee if alertness is low and it's safe for blood pressure
    if alertness < 0.6 and hypertension < 0.05:
        return 1  # Coffee to boost alertness moderately

    # Drink beer only when safe and health indicators are optimal
    if alertness > 0.8 and intoxication < 0.03 and hypertension < 0.02:
        return 2  # Reward with beer in optimal state

    return 0  # Default to work when conditions are generally stable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)