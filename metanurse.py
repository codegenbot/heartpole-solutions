import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep based more stringently on alertness and intoxication
    if alertness < 0.4 or time_since_slept >= 4 or intoxication > 0.1:
        return 3  # Sleep when alertness is very low, sleep deprived, or intoxicated.

    # Use coffee when alertness is low, but ensure hypertension level is safe
    if alertness < 0.6 and hypertension < 0.03:
        return 1  # Drink coffee to boost alertness safely.

    # Avoid beer if hypertension is risky or intoxication is noticeable
    if 0.65 <= alertness < 0.75 and intoxication < 0.05 and hypertension < 0.02:
        return 2  # Drink beer cautiously.

    # Default to working if all health indicators are stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)