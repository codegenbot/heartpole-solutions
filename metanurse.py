import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleeping under these conditions
    if time_since_slept > 5 or hypertension > 0.5 or alertness < 0.3 or intoxication > 0.5:
        return 3  # Sleep when too tired, stressed, or intoxicated
    # Prefer working only in optimal conditions
    if alertness > 0.8 and hypertension < 0.35 and intoxication <= 0.05:
        return 0  # Work only
    # Allow coffee use sparingly and when safe
    if alertness < 0.5 and hypertension < 0.3 and intoxication <= 0.2:
        return 1  # Drink coffee and work if necessary
    # Avoid drinking beer when intoxicated
    if alertness < 0.4 and hypertension < 0.25 and intoxication <= 0.3:
        return 2  # Drink beer and work otherwise
    return 0  # Default to work if no other conditions

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)