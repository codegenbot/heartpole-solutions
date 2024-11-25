import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep to prevent health deterioration
    if time_since_slept > 12 or alertness < 0.3 or hypertension > 0.7 or intoxication > 0.5:
        return 3  # Sleep

    # Drink beer if hypertension slightly high but under control
    if 0.5 < hypertension <= 0.7 and intoxication <= 0.6:
        return 2  # Drink beer and work to slightly reduce hypertension

    # If conditions are safe and productive, just work
    if alertness >= 0.6 and hypertension < 0.6 and intoxication < 0.4:
        return 0  # Just work

    # Use coffee to boost alertness if moderate
    if 0.35 <= alertness < 0.6 and hypertension < 0.7 and intoxication < 0.5:
        return 1  # Drink coffee and work

    # Default to sleep if uncertainties are present
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)