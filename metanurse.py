import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep to improve overall health
    if (
        alertness < 0.6
        or hypertension > 0.06
        or intoxication > 0.05
        or time_since_slept >= 3.5
    ):
        return 3  # Sleep if any health indicators are concerning.

    # Drink beer to decrease stress when hypertension is low
    if alertness < 0.7 and intoxication <= 0.06 and hypertension > 0.04:
        return 2  # Relax with a beer if mildly stressed.

    # Use coffee to boost alertness and productivity safely
    if 0.4 <= alertness < 0.8 and hypertension < 0.03:
        return 1  # Drink coffee for a slight productivity boost.

    # Default to work if conditions allow without significant health risk
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)