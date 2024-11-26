import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate health concerns take precedence
    if hypertension > 0.015 or intoxication > 0.07:
        return 3  # Immediate rest is necessary
    
    # Ensure regular sleep for optimal function
    if time_since_slept >= 4:
        return 3  # Prioritize sleep if awake for a prolonged period
    
    # If alertness is really low, rest is better than stimulants long-term
    if alertness < 0.3:
        return 3  # Rest is required for very low alertness
    
    # Manage alertness with coffee responsibly
    if 0.4 <= alertness < 0.5 and hypertension < 0.008:
        return 1  # Use coffee to boost alertness cautiously
    
    # Optimize performance when appropriately alert
    if 0.5 <= alertness < 0.85 or (work_done > 8.0 and time_since_slept < 4):
        return 0  # Focus on work efficiently
    
    # Default action to just work if no immediate health concerns or need for rest
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)