import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if any health or alertness thresholds are critically low
    if (
        alertness < 0.6
        or hypertension > 0.08
        or intoxication > 0.05
        or time_since_slept >= 4
    ):
        return 3  # Sleep if any health indicators are concerning.

    # Use coffee to boost alertness when needed and safe
    if alertness < 0.7 and hypertension < 0.05:
        return 1  # Drink coffee to boost productivity when it's safe.

    # Avoid beer unless it provides a balance with other factors
    if 0.7 <= alertness < 0.75 and hypertension <= 0.06 and intoxication <= 0.02:
        return 2  # Drink beer carefully balancing other health metrics.

    # Default to work if conditions remain stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)