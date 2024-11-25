import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if critical health conditions are met
    if (alertness < 0.25 or hypertension > 0.75 or intoxication > 0.5 or time_since_slept > 10):
        return 3  # Need sleep

    # If conditions support productivity well, just work
    if alertness > 0.85 and hypertension < 0.5 and intoxication < 0.05:
        return 0  # Just work

    # Use coffee to boost alertness moderately for better work capacity
    if 0.3 <= alertness < 0.8 and hypertension < 0.6 and intoxication < 0.15:
        return 1  # Coffee and work

    # If mildly influenced, sleep to reset for better health recovery
    if intoxication > 0.2:
        return 3  # Sleep

    # Default to sleep for consistent recovery support
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)