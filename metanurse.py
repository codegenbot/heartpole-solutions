import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Emphasize sleep when alertness is low or any health metric is critical
    if (
        hypertension >= 0.3
        or intoxication >= 0.25
        or time_since_slept >= 8
        or alertness < 0.4
    ):
        return 3  # Sleep

    # Use coffee wisely to optimize alertness without hypertension risk
    if alertness < 0.6 and hypertension < 0.15:
        return 1  # Drink coffee and work

    # Maintain a good working condition with optimal health
    if alertness >= 0.7 and hypertension < 0.1 and intoxication < 0.05:
        return 0  # Just work

    # Default to resting more frequently to prevent health risks
    return 3  # Sleep


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)