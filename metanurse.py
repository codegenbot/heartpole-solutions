import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if nearing a critical threshold
    if (
        alertness < 0.45
        or time_since_slept >= 5.5
        or intoxication > 0.1
        or hypertension > 0.07
    ):
        return 3  # Sleep to recover

    # Drink coffee if alertness is moderately low and it's safe for blood pressure
    if alertness < 0.65 and hypertension < 0.04:
        return 1  # Coffee to boost alertness

    # Avoid rewarding with beer unless both alertness and health indicators are optimal
    if alertness > 0.85 and intoxication < 0.02 and hypertension < 0.015:
        return 2

    return 0  # Default to just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)