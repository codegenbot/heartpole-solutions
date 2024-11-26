import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if alertness is low or sleep deprived
    if alertness < 0.5 or time_since_slept >= 3:
        return 3  # Sleep when alertness is very low or sleep deprived.

    # Use coffee only when moderately tired and safe for hypertension
    if alertness < 0.6 and hypertension < 0.04:
        return 1  # Drink coffee to boost productivity safely.

    # Avoid beer if intoxication is noticeable
    if 0.65 <= alertness < 0.75 and intoxication <= 0.01:
        return 2  # Drink beer with caution, only when barely needed.

    # Default to working if all indicators are stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)