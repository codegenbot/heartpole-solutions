import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if health issues are above any critical threshold
    if hypertension > 0.6 or intoxication > 0.4:
        return 3  # Sleep to mitigate serious health risks
    
    # If awake for over 15 hours and alertness or other health indicators suggest rest
    if time_since_slept > 15 or (alertness < 0.4 and time_elapsed >= 14):
        return 3  # Sleep to recover alertness and productivity
    
    # Use coffee strategically when alertness is low and work needs doing
    if alertness < 0.5:
        if time_elapsed < 9:  # Consider a longer work period with coffee
            return 1  # Drink coffee and work for boost
    
    # Default work if alert and work isn't complete but within healthy limits
    if alertness >= 0.5 and work_done < 0.8:
        return 0  # Work if alert enough and there is work left
    
    # Otherwise, consider quick recovery actions like brief rest for better productivity
    return 3 if alertness < 0.6 else 0  # Rest if slightly alert, work otherwise

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)