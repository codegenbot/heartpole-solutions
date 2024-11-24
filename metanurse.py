import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping earlier to prevent health issues
    if (
        alertness < 0.75
        or hypertension > 0.6
        or intoxication > 0.25
        or time_since_slept >= 4
    ):
        return 3  # Must sleep

    # Allow working if all health metrics are in check
    if alertness > 0.8 and hypertension < 0.4 and intoxication < 0.1:
        return 0  # Just work

    # Use coffee as a controlled alertness booster when safe
    if alertness <= 0.7 and hypertension <= 0.45:
        return 1  # Drink coffee and work

    return 0  # Default to work without additional actions

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)