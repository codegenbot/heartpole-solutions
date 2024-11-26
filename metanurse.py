import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep immediately if alertness is low or sleep deprived
    if alertness < 0.5 or time_since_slept >= 2:
        return 3  # Sleep when alertness is low or sleep deprived.

    # Use coffee only when moderately tired and hypertension is very low
    if alertness < 0.6 and hypertension < 0.02:
        return 1  # Drink coffee to boost productivity safely.

    # Avoid beer if intoxication is noticeable or alertness is not ideal
    if 0.65 <= alertness < 0.75 and intoxication < 0.005:
        return 2  # Drink beer cautiously.

    # Default to just working if all health indicators are stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)