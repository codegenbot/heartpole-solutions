import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep for recovery if exhausted or nearly so
    if time_since_slept >= 8 or alertness < 0.4:
        return 3  # Sleep

    # Address dangerous hypertension levels, balancing with intoxication
    if hypertension > 0.9:
        if intoxication < 0.5:
            return 2  # Manage hypertension with beer if not high on intoxication
        else:
            return 3  # Sleep is a safer option if intoxication is high

    # Use coffee to enhance alertness in safe ranges
    if alertness < 0.6 and hypertension < 0.7 and intoxication < 0.3:
        return 1  # Drink coffee and work

    # Work optimally if energy and health conditions allow
    if alertness >= 0.7 and hypertension <= 0.5 and intoxication <= 0.2:
        return 0  # Just work

    # If slightly raised health indicators, prefer stabilizing with beer
    if hypertension > 0.6 and intoxication < 0.3:
        return 2  # Drink beer and work

    # Default: sleep if conditions are ambiguous
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)