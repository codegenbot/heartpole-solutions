import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep to improve overall health and handle slight intoxication.
    if (
        alertness < 0.65
        or hypertension > 0.05
        or intoxication > 0.04
        or time_since_slept >= 3.0
    ):
        return 3  # Sleep if any health indicators are concerning.

    # Avoid coffee if alert enough and allow it only for moderate hypertension.
    if alertness < 0.7 and hypertension < 0.02:
        return 1  # Drink coffee if alertness or productivity truly needs a boost.

    # Avoid using beer unless stress (hypertension) is very specific.
    if 0.6 <= alertness < 0.75 and 0.03 <= hypertension <= 0.05 and intoxication <= 0.03:
        return 2  # Relax with a beer only in very specific low-stress windows.

    # Default to work if conditions are sustainable.
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)