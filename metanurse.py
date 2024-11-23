import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize health issues immediately
    if hypertension > 0.2 or intoxication > 0.2:
        return 3  # Sleep

    # Rest if alertness is significantly low or too much time since last sleep
    if alertness < 0.4 or time_since_slept > 8:
        return 3  # Sleep
    
    # Use coffee if alertness is low and it's early or mid-session
    if alertness < 0.6 and time_elapsed < 8:
        return 1  # Drink coffee and work
    
    # Consider beer only if nearing completion, conditions allow a morale boost
    if work_done > 0.9 and intoxication < 0.05 and time_elapsed >= 8:
        return 2  # Drink beer and work
    
    # Continue working if all conditions are favorable or satisfactory
    if alertness >= 0.6 and hypertension <= 0.15 and intoxication <= 0.05:
        return 0  # Just work
    
    # Default to sleep when confused by conditions
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)