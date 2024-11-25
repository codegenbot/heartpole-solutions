import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize Sleep Aggressively
    if time_since_slept > 3 or alertness < 0.5 or hypertension > 0.5 or intoxication > 0.3:
        return 3  # Sleep
    
    # Balance Alertness with Hypertension for coffee
    if alertness < 0.7 and hypertension <= 0.4 and intoxication <= 0.2:
        return 1  # Drink coffee and work
    
    # Condition for Default Work should maintain a healthy and alert state
    if alertness >= 0.8 and hypertension <= 0.25 and intoxication <= 0.1:
        return 0  # Just work
    
    # Beer condition without exceeding manageable health risks
    if alertness < 0.7 and hypertension < 0.3 and intoxication <= 0.3:
        return 2  # Drink beer and work

    return 0  # Default action is just work for any unhandled condition

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)