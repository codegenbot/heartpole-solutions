import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep when urgent
    if time_since_slept > 10 or alertness < 0.5:
        return 3  # Sleep
    
    # Prevent work when health metrics are risky
    if hypertension > 0.15 or intoxication > 0.06:
        return 3  # Sleep

    # Increase coffee usage slightly for productivity
    if alertness < 0.7 and hypertension <= 0.1 and intoxication <= 0.05:
        return 1  # Drink coffee and work

    # Set tighter condition for safe beer consumption
    if alertness >= 0.9 and hypertension <= 0.05 and intoxication < 0.02:
        return 2  # Drink beer and work

    # Default to working in generally healthy conditions
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)