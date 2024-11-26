import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize severe health risks:
    if hypertension > 0.05 or intoxication > 0.04:
        return 3  # Sleep to recover from serious health issues

    # Favor sleep if too long without rest or moderate health risks:
    if time_since_slept > 8 or (hypertension > 0.03 and intoxication > 0.03):
        return 3

    # Use coffee to boost alertness effectively:
    if alertness < 0.7 and hypertension < 0.03 and intoxication < 0.02:
        return 1

    # Work if alertness and health conditions are very good:
    if alertness >= 0.8 and hypertension < 0.015 and intoxication < 0.015:
        return 0

    # If alertness moderately drops, balance work with minor beer consumption:
    if alertness < 0.75:
        return 2

    # Default to sleep if no other condition is met:
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)