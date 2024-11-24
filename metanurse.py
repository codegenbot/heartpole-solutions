import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if any serious health issue
    if alertness < 0.4 or hypertension > 0.7 or intoxication > 0.5 or time_since_slept > 8:
        return 3
    
    # Drink Coffee and Work: balance alertness and hypertension
    if 0.5 <= alertness <= 0.7 and hypertension < 0.5 and intoxication < 0.25:
        return 1

    # Just Work: high alertness with safe health levels
    if alertness > 0.7 and hypertension < 0.5 and intoxication < 0.2 and time_since_slept <= 5:
        return 0

    # Drink Beer and Work: attempt to reduce hypertension
    if alertness < 0.5 and intoxication < 0.1 and hypertension < 0.4:
        return 2

    # Default to sleep if conditions do not satisfy any productivity action
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)