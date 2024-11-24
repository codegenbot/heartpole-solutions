import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.4 or hypertension > 0.8 or intoxication > 0.5 or time_since_slept > 8:
        return 3  # Sleep is essential for recovery
    if alertness < 0.6 and hypertension < 0.75 and intoxication < 0.25:
        return 1  # Use coffee prudently to slightly boost alertness
    if alertness >= 0.7 and hypertension < 0.7 and intoxication < 0.2:
        return 0  # Conditions are good for working
    if 0.5 <= alertness < 0.7 and hypertension < 0.6 and intoxication < 0.3:
        return 0  # Acceptable to work in moderate conditions
    if hypertension < 0.5 and intoxication < 0.3:
        return 2  # Consider beer if stress relief is beneficial
    return 3  # Default to sleep when unsure to avoid negative impacts

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)