import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleeping for critical health issues or poor alertness
    if alertness < 0.5 or hypertension >= 0.03 or intoxication > 0.15 or time_since_slept >= 7:
        return 3  # Sleep
    
    # Coffee can boost alertness if moderate but hypertension and intoxication are low
    if 0.5 <= alertness < 0.8 and hypertension < 0.02 and intoxication < 0.1:
        return 1  # Drink coffee and work
    
    # If alertness is very good, just work
    if alertness >= 0.8 and hypertension < 0.02 and intoxication < 0.1 and time_since_slept < 6:
        return 0  # Just work
    
    # As a fallback, ensure to prioritize reducing intoxication
    if intoxication >= 0.1:
        return 2  # Drink beer and work
    
    return 0  # Default to just work if no other explicit conditions are triggered

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)