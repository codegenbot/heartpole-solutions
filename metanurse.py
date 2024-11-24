import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if any serious health issue
    if hypertension > 0.6 or intoxication > 0.6 or time_since_slept > 12:
        return 3
    
    # Require sleep if very low alertness or excessive time awake
    if alertness < 0.5:
        return 3
    
    # Drink coffee to safely boost alertness
    if alertness < 0.7 and hypertension < 0.5 and intoxication < 0.4:
        return 1
    
    # If safe, just work with optimal conditions
    if alertness >= 0.7 and hypertension <= 0.4 and intoxication <= 0.3:
        return 0
    
    # When moderate conditions, risk beer only if alertness is not too low
    if alertness >= 0.5:
        return 2

    # Default to sleep if unsure
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)