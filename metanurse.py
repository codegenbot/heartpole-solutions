import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if any critical health or alertness thresholds approach
    if (
        alertness < 0.5
        or hypertension > 0.07
        or intoxication > 0.04
        or time_since_slept >= 3.5
    ):
        return 3  # Sleep if any health indicators are concerning.

    # Use coffee if alertness is moderate and hypertension is low
    if 0.5 <= alertness < 0.7 and hypertension < 0.04:
        return 1  # Drink coffee for a productivity boost.

    # Avoid using beer unnecessarily; check all health conditions are safe
    if 0.5 <= alertness < 0.55 and hypertension <= 0.06 and intoxication <= 0.04:
        return 2  # Drink beer if it will not tilt health adversely.

    # Default to work if conditions are stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)