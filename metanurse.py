import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 5 or hypertension > 0.5 or intoxication > 0.3:
        return 3  # Sleep if risk to health is identified
    if alertness < 0.5 and time_since_slept <= 5 and intoxication < 0.2:
        return 1  # Drink coffee to boost alertness
    return 0  # Default to working if conditions are safe

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)