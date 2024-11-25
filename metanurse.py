import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleeping if alertness is too low or it has been a while since sleeping
    if alertness < 0.4 or time_since_slept > 5:
        return 3
    
    # Use coffee to improve alertness but be cautious with health factors
    if alertness < 0.5 and hypertension < 0.1 and intoxication < 0.03:
        return 1
        
    # Work if conditions are ideal
    if alertness >= 0.6 and hypertension < 0.12 and intoxication < 0.04:
        return 0
    
    # Use beer cautiously as a last resort when work_done is low
    if alertness > 0.5 and intoxication < 0.02 and work_done < 0.15:
        return 2

    # Default to work if no conditions are met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)