import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Dangerously high health indicators require immediate rest
    if hypertension > 0.6 or intoxication > 0.4:
        return 3  # Sleep to mitigate high health risks
    
    # Sleep if very tired or awake too long
    if time_since_slept > 12 or (alertness < 0.2 and time_elapsed >= 16):
        return 3
    
    # Use coffee conservatively for boosting alertness in reasonable hours
    if alertness < 0.5 and time_elapsed < 10:
        return 1
    
    # Only drink beer when alertness is at a sustainable level and minor stress relief needed
    if alertness >= 0.5 and intoxication < 0.1 and time_elapsed > 15:
        return 2

    # If work is significantly incomplete, prioritize work but ensure moderate alertness
    if alertness >= 0.5 and work_done < 0.8:
        return 0
    
    # Rest if no urgent work and low alertness
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)