import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if any health risk is detected
    if (
        hypertension > 0.6 
        or intoxication > 0.2 
        or time_since_slept > 8
        or alertness < 0.35
    ):
        return 3  # Sleep
    
    # Use coffee only if it boosts alertness and health levels are acceptable
    if (
        alertness < 0.6
        and hypertension < 0.4
        and intoxication < 0.1
    ):
        return 1  # Drink coffee and work
    
    # Work directly if all conditions are favorable
    if alertness >= 0.7 and hypertension < 0.3 and intoxication < 0.05:
        return 0  # Just work
    
    # Avoid unnecessary beer action, prioritize other actions
    return 0  # Default action is to just work if no specific risk is evident

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)