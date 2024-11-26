import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep for significant hypertension or intoxication
    if hypertension > 0.02 or intoxication > 0.1:
        return 3  # sleep to address health risks
    
    # Sleep for alertness improvement or significant sleep deprivation
    if time_since_slept >= 6 or alertness < 0.3:
        return 3  # sleep to restore sleep hygiene and alertness   
    
    # Consider coffee when alert and healthy enough for productivity boost
    if alertness < 0.65 and hypertension < 0.015 and intoxication < 0.07:
        return 1  # boost alertness with coffee within safer limits
    
    # Default to working under optimal conditions
    return 0  # just work otherwise

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)