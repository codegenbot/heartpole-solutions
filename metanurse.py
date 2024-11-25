import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for extreme conditions
    if time_since_slept > 8 or alertness < 0.5 or hypertension > 0.8 or intoxication > 0.3:
        return 3  # Sleep is prioritized if conditions are risky
    
    # Use coffee to boost alertness when it's moderately low and safe conditions
    if alertness < 0.75 and time_since_slept <= 8 and hypertension < 0.6 and intoxication < 0.15:
        return 1  # Drink coffee and work if safe and alertness needs a boost
    
    # Default to work if conditions are good
    if alertness >= 0.75 and hypertension < 0.3 and intoxication < 0.1:
        return 0  # Just work if all conditions are good
    
    # Use beer if intoxication needs to be managed slightly
    if intoxication >= 0.15 and intoxication < 0.3:
        return 2  # Drink beer and work if intoxication is mild and needs managing
    
    return 0  # Default action is to just work if no specific condition is met

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)