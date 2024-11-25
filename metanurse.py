import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep more aggressively
    if hypertension > 0.25 or intoxication > 0.15 or alertness < 0.6 or time_since_slept > 5:
        return 3
    
    # Drink coffee with more conservative conditions
    if alertness < 0.8 and hypertension < 0.15 and intoxication < 0.05:
        return 1
    
    # Drink beer more cautiously and less frequently
    if alertness >= 0.8 and hypertension < 0.15 and intoxication == 0.0 and work_done < 0.4:
        return 2
    
    # Default to working if conditions are optimal
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)