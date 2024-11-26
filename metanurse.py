import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if nearing any critical health or alertness thresholds
    if (
        alertness < 0.5
        or hypertension > 0.06
        or intoxication > 0.03
        or time_since_slept >= 3
    ):
        return 3  # Sleep if any health indicators are concerning.

    # Use coffee carefully; balance increased hypertension risk
    if 0.6 <= alertness < 0.7 and hypertension < 0.03:
        return 1  # Drink coffee for a moderate productivity boost safely.

    # Highly restrict beer use to very specific safe conditions
    if 0.55 <= alertness < 0.6 and hypertension <= 0.05 and intoxication <= 0.03:
        return 2  # Drink beer if minimal risk and close to needing sleep.

    # Default to work if conditions are stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)