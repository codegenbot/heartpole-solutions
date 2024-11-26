import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Always prioritize sleep when health indicators suggest risk
    if (
        alertness < 0.5      # Ensure high enough alertness for effective work
        or hypertension > 0.07 # Lower the threshold to rest before hypertension becomes critical
        or intoxication > 0.05 # Same threshold to prevent risk from intoxication
        or time_since_slept >= 3.5  # Sleep sooner if restless
    ):
        return 3  # Sleep to recuperate if any concerning indicators are present.

    # Drink coffee if moderate alertness without hypertension risk
    if 0.5 <= alertness < 0.8 and hypertension < 0.05:
        return 1  # Use coffee for increased alertness, avoiding caffeine-induced hypertension

    # Default to work if conditions are adequately safe
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)