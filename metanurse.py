import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize necessary sleep
    if time_since_slept >= 4.5 or alertness < 0.4:
        return 3  # Sleep when very sleep-deprived or very low alertness.

    # Further manage hypertension and intoxication tolerance
    if intoxication > 0.06 or hypertension > 0.04:
        return 3  # Sleep to recover from moderate intoxication or hypertension.

    # Use coffee cautiously, with stricter alertness needs
    if alertness < 0.6 and hypertension < 0.02:
        return 1  # Drink coffee for alertness improvements when safe.

    # Default to just work when health is fairly stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)