import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize health conditions
    if hypertension > 0.02 or intoxication > 0.10:
        return 3  # Sleep to address health warnings

    # If very low alertness, prioritize sleep for recovery
    if alertness < 0.3:
        return 3  # Sleep

    # Initiate sleep when alertness is low or sleep overdue
    if time_since_slept > 7:
        return 3  # Sleep

    # Use coffee to boost medium alertness, ensuring health is stable
    if 0.3 <= alertness < 0.5 and hypertension < 0.02:
        return 1  # Coffee and work

    # Opt to work if conditions are stable
    if alertness >= 0.5 and intoxication < 0.1:
        return 0  # Work safely without coffee

    return 3  # Favor sleep otherwise

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)