import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if any of these critical conditions are met
    if alertness < 0.3 or hypertension > 0.15 or intoxication > 0.20 or time_since_slept > 8:
        return 3  # Sleep
    
    # Consider sleep if the alertness is mildly low or if hasn't slept for a long time
    if alertness < 0.5 or time_since_slept > 6:
        return 3  # Sleep
    
    # Drink coffee and work if alertness is mid-level and health parameters are in safe range
    if alertness < 0.7 and hypertension < 0.10:
        return 1  # Drink coffee and work

    # Only work if alertness is high and health parameters are good
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)