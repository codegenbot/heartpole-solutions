import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize health conditions
    if hypertension > 0.05 or intoxication > 0.2:
        return 3  # Sleep to address severe health warnings

    # Consider sleep necessity
    if time_since_slept >= 10 or alertness < 0.3:
        return 3  # Sleep for recovery

    # Use coffee at lower alertness levels to boost it
    if alertness < 0.5:
        return 1  # Coffee and work to increase alertness

    # Opt to work if conditions are stable
    if alertness >= 0.5 and intoxication < 0.1:
        return 0  # Work safely without coffee

    return 0  # Default to working when conditions are stable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)