import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize health conditions but allow some leeway
    if hypertension > 0.03:
        return 3  # Sleep if hypertension too high
    if intoxication > 0.12:
        return 3  # Sleep if intoxication too high

    # If very low alertness, prioritize sleep
    if alertness < 0.25:
        return 3

    # Initiate sleep after a long time without sleep
    if time_since_slept > 10:
        return 3

    # Use coffee to boost medium alertness
    if alertness < 0.6 and hypertension < 0.03 and work_done < 80:
        return 1  # Use coffee when feasible to work efficiently

    # Opt to work if conditions are stable
    if alertness >= 0.5:
        return 0

    # Default to sleep if nothing else
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)