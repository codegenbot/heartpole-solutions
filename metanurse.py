import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate health concerns take precedence
    if hypertension > 0.01 or intoxication > 0.05:
        return 3  # Immediate rest is necessary for health concerns
    
    # Regular sleep: prioritize more frequently to prevent cumulative Sleep debt
    if time_since_slept >= 3:
        return 3  # Encourage more frequent rest
    
    # If alertness is low, rest should be prioritized over work
    if alertness < 0.4:
        return 3  # Rest if alertness drops significantly
    
    # Manage alertness and prevent reliance on coffee
    if 0.4 <= alertness < 0.6 and hypertension < 0.008 and intoxication < 0.03:
        return 1  # Moderate use of coffee if necessary
    
    # Optimize performance when alertness is at an optimal level
    if 0.6 <= alertness < 0.85:
        return 0  # Focus directly on work
    
    # Default action to just work if no immediate concerns
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)