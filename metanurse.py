import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate health concerns take precedence.
    if hypertension > 0.020 or intoxication > 0.08:
        return 3  # Immediate rest is necessary.
    
    # Ensure regular sleep for optimal function.
    if time_since_slept >= 5:
        return 3  # Prioritize sleep if awake for a prolonged period.
    
    # If alertness is low, rest is better than stimulants long-term.
    if alertness < 0.3:
        return 3  # Rest is required for very low alertness.
    
    # Manage alertness with coffee responsibly.
    if alertness < 0.6 and hypertension < 0.010:
        return 1  # Use coffee to boost alertness cautiously.
    
    # Optimize performance when appropriately alert.
    if 0.6 <= alertness < 0.85:
        return 0  # Focus on work efficiently.
    
    # Minimize adverse effects with default action being work.
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)