import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.02 or intoxication > 0.1:
        return 3  # Prioritize sleep for health recovery
    if time_since_slept >= 6 or alertness < 0.3:
        return 3  # Sleep for recovery
    if alertness < 0.6 and hypertension < 0.01 and intoxication < 0.05:
        return 1  # Use coffee to boost alertness safely
    return 0  # Default to just working

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)