import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if low alertness or high hypertension or intoxication
    if alertness < 0.5 or hypertension > 0.5 or intoxication > 0 or time_since_slept > 4.5:
        return 3  # Sleep
    
    # Just work when in optimal conditions
    if alertness >= 0.9 and hypertension < 0.25 and intoxication == 0.0:
        return 0  # Just work

    # Drink coffee if moderate alertness and low health risks
    if 0.65 <= alertness < 0.85 and hypertension < 0.4 and intoxication == 0.0:
        return 1  # Drink coffee and work

    # Avoid beer unless slightly low alertness and very low health risks
    if 0.5 <= alertness < 0.65 and intoxication == 0.0 and hypertension < 0.3:
        return 2  # Drink beer and work

    # Default to sleep if none of the above conditions are met
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)