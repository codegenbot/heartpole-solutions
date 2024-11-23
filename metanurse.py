import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate health risks prioritized
    if hypertension > 0.25 or intoxication > 0.12 or time_since_slept > 5.5:
        return 3  # Sleep

    # Requirement to rest further if alertness falls below a sharper threshold
    if alertness < 0.55:
        return 3  # Sleep

    # Use coffee cautiously without harsh thresholds
    if 0.55 <= alertness < 0.75 and hypertension <= 0.2 and intoxication <= 0.08:
        return 1  # Drink coffee and work

    # Avoid alcohol unless more stringent scenarios apply
    if alertness < 0.65 and intoxication <= 0.10:
        return 0  # Just work

    # Default safe productive state
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)