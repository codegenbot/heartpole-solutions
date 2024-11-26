import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize health conditions
    if hypertension > 0.03 or intoxication > 0.15:
        return 3  # Sleep to address health warnings

    # Consider sleep necessity
    if time_since_slept >= 8 or alertness < 0.4:
        return 3  # Sleep for recovery

    # Use coffee to boost alertness without risking health
    if 0.4 <= alertness < 0.6 and hypertension < 0.03:
        return 1  # Coffee and work

    # Opt to work if conditions are stable
    if alertness >= 0.6 and intoxication < 0.1:
        return 0  # Work safely without coffee

    return 0  # Default to working when conditions are stable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)