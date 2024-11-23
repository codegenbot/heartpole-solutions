import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Enforce sleep for any critical health risks
    if hypertension > 0.25 or intoxication > 0.2 or time_since_slept > 6:
        return 3  # Sleep

    # Enforce sleep if alertness is critically low
    if alertness < 0.5:
        return 3  # Sleep

    # Drink coffee to boost alertness safely without high risks
    if alertness < 0.7 and hypertension < 0.25 and intoxication < 0.15:
        return 1  # Drink coffee and work

    # Drink beer only if intoxication is manageable and you are alert
    if intoxication > 0.15 and alertness >= 0.7 and hypertension < 0.15:
        return 2  # Drink beer and work

    # Default to working if all conditions are satisfied
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)