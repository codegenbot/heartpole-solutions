import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if necessary
    if time_since_slept > 5 or alertness < 0.6 or hypertension > 0.25 or intoxication > 0.05:
        return 3  # Sleep is necessary
    
    # Allow coffee when alertness is a bit low but conditions are safe
    if alertness < 0.75 and hypertension < 0.2 and intoxication < 0.03 and time_since_slept <= 3:
        return 1  # Drink coffee to boost alertness safely
    
    # Avoid coffee if nearing hypertension risk
    if alertness < 0.7 and hypertension < 0.2:
        return 0  # Just work, avoiding coffee
    
    return 0  # Default to work for productivity

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)