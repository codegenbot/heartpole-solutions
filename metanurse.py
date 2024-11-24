import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep for low alertness or excessive time without sleep
    if time_since_slept >= 8 or alertness < 0.6:
        return 3  # Sleep

    # Consider coffee if alertness is low but within safe parameters for hypertension and intoxication
    if alertness < 0.7 and hypertension <= 0.5 and intoxication < 0.3:
        return 1  # Drink coffee and work

    # Avoid beer if hypertension is high; otherwise, only use it to work if needed to relax (productivity risk)
    if hypertension > 0.7:
        return 3  # Sleep instead to mitigate risk
    elif hypertension > 0.4 and alertness >= 0.5 and intoxication < 0.3:
        return 2  # Drink beer and work
    
    # If conditions are optimal, focus on work
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.2:
        return 0  # Just work

    return 3  # Default to sleep if unsure, for health safety

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)