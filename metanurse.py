import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.5 or hypertension > 0.15 or intoxication > 0.05 or time_since_slept > 6:
        return 3  # Prioritize sleep if any critical condition is met
    if alertness < 0.7 and hypertension < 0.1 and intoxication < 0.03:
        return 1  # Use coffee to boost alertness under safe conditions
    if hypertension < 0.08 and intoxication < 0.02:
        return 0  # Default to just work if conditions are safe
    return 0  # Fallback to just work if no other condition is satisfied

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)