import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for severe conditions or low alertness
    if hypertension >= 0.25 or intoxication >= 0.2 or alertness < 0.4:
        return 3  # Sleep

    # Encourage sleep based on longer time since last slept
    if time_since_slept >= 3:
        return 3  # Sleep

    # Use coffee if alertness needs boosting and hypertension is low
    if alertness < 0.5 and hypertension < 0.2:
        return 1  # Drink coffee and work

    # Work primarily when in good health parameters
    if alertness >= 0.6 and hypertension < 0.15 and intoxication < 0.1:
        return 0  # Just work

    # If intoxication is extremely low, consider beer to boost mood
    if intoxication < 0.05 and alertness < 0.6:
        return 2  # Drink beer and work

    # Default to working or sleeping based on alertness
    return 0 if alertness >= 0.5 else 3  # Just work or Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)