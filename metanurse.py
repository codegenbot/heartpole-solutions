import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if health metrics reach critical levels, prioritize long-term health
    if (
        alertness < 0.3
        or hypertension > 0.8
        or intoxication > 0.5
        or time_since_slept > 6
    ):
        return 3

    # Drink coffee if alertness is low and moderate levels of hypertension allow it
    if (
        alertness < 0.5
        and hypertension < 0.6
        and intoxication < 0.2
    ):
        return 1

    # Only work when alert, and all health indicators are well below critical
    if alertness >= 0.6 and hypertension < 0.5 and intoxication < 0.3:
        return 0

    # Adjust beer consumption decision to act when intoxication is within manageable thresholds
    if hypertension < 0.5 and 0.2 <= intoxication < 0.4:
        return 2

    # Default to sleep when unsure, allowing health metrics to recover
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)