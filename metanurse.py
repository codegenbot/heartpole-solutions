import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Priority check for health issues
    if hypertension > 0.5 or intoxication > 0.2:
        return 3  # Sleep if significant health issues exist
    
    # Encourage sleep when alertness is low or extensive awake periods
    if alertness < 0.5 or time_since_slept > 10:
        return 3  # Sleep if alertness is low or awake too long
    
    # Productiveness with sufficient alertness
    if alertness >= 0.7 and work_done < 0.8:
        return 0  # Just work if alert and work is not completed
    
    # Use coffee judiciously when alertness is moderate
    if alertness < 0.6 and time_elapsed < 8 and time_since_slept <= 6:
        return 1  # Drink coffee and work only earlier in the wake cycle
        
    return 0  # Default to just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)