import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health by ensuring sleep when necessary
    if time_since_slept >= 4.5 or alertness < 0.5:
        return 3  # Sleep when significantly sleep-deprived or very low alertness.

    # Avoid increasing intoxication and hypertension unnecessarily
    if intoxication > 0.07 or hypertension > 0.05:
        return 3  # Sleep to recover from high intoxication or hypertension.

    # Moderate coffee consumption to manage alertness and hypertension
    if alertness < 0.65 and hypertension < 0.03:
        return 1  # Use coffee cautiously to maintain alertness.

    # Default to work when health indicators are stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)