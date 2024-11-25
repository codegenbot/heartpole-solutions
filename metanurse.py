import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if critical health conditions exist
    if alertness < 0.4 or hypertension > 0.75 or intoxication > 0.45 or time_since_slept > 10:
        return 3  # Sleep
    
    # Optimal conditions for just working
    if alertness >= 0.8 and hypertension < 0.55 and intoxication < 0.15:
        return 0  # Just work
    
    # Drink coffee to boost productivity when moderately tired
    if 0.6 <= alertness < 0.8 and hypertension < 0.65 and intoxication < 0.25:
        return 1  # Coffee and work
    
    # If alertness is low and there's no immediate need for sleep, utilize beer cautiously
    if alertness < 0.6 and hypertension < 0.5 and intoxication < 0.3 and time_since_slept <= 9:
        return 2  # Beer and work
    
    # Default action is to sleep in uncertain/risky situations
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)