import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep for low alertness or excessive time without sleep
    if time_since_slept >= 7 or alertness < 0.5:
        return 3  # Sleep

    # Consider coffee if alertness is moderately low, guarding against hypertension and intoxication
    if alertness < 0.65 and hypertension <= 0.5 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Avoid beer if hypertension is high, use it to manage moderate hypertension and low intoxication
    if hypertension > 0.65:
        return 3  # Sleep to mitigate risk
    elif hypertension > 0.4 and alertness >= 0.5 and intoxication < 0.25:
        return 2  # Drink beer and work
    
    # If conditions are optimal, focus on work
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.15:
        return 0  # Just work

    return 3  # Default to sleep if health parameters are borderline

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)