import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if severely lacking
    if time_since_slept >= 8 or alertness < 0.4:
        return 3  # Sleep

    # Use coffee to boost alertness but avoid if hypertension is high
    if alertness < 0.6 and hypertension <= 0.6 and intoxication < 0.3:
        return 1  # Drink coffee and work

    # Use beer to calm if hypertension is a concern but avoid if intoxication is near danger levels
    if hypertension > 0.7 and intoxication < 0.2:
        return 2  # Drink beer and work

    # Optimal state for working only if in a healthy condition
    if alertness >= 0.8 and hypertension < 0.5 and intoxication < 0.15:
        return 0  # Just work

    # Sleep if conditions indicate risk of poor health/performance
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)