import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.7 or intoxication > 0.6:  # Be more cautious with high health risks
        return 3  # Sleep
    
    if alertness < 0.4 or time_since_slept > 10:  # If very tired, prioritize sleep
        return 3  # Sleep
    
    if alertness < 0.7 and hypertension < 0.5:  # Consider coffee for mild alertness drop and safe hypertension
        return 1  # Drink coffee and work
    
    if alertness >= 0.5 and hypertension < 0.4 and intoxication < 0.15:
        return 0  # Just work in optimal conditions
    
    # Avoid using beer unless specific target met, as it increases intoxication:
    if alertness < 0.5 and intoxication < 0.1:
        return 2  # Drink beer and work

    return 3  # Default to sleep if conditions are not ideal for other actions

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)