import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritizing sleep more aggressively
    if hypertension > 0.3 or intoxication > 0.3 or time_since_slept > 6:
        return 3  # Sleep if any health condition is moderately high or long awake time

    if alertness < 0.4 and hypertension < 0.2 and intoxication < 0.15:
        return 1  # Drink coffee when alertness is low but under safe conditions

    if alertness >= 0.6 and hypertension < 0.2 and intoxication < 0.1:
        return 0  # Work when alertness is optimal, prioritizing productivity

    # Allow beer when work is high and conditions are safe enough
    if work_done > 10 and alertness > 0.4 and intoxication < 0.15 and hypertension < 0.2:
        return 2  # Drink beer, allowing downtime under moderate work and safe health
    
    return 3  # Default action to sleep if no other conditions are met

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)