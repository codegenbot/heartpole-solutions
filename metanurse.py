import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep for severe sleep deprivation or very low alertness
    if alertness < 0.3 or time_since_slept > 6:
        return 3
    
    # Use coffee if it boosts alertness without serious health risks
    if alertness < 0.5 and hypertension < 0.15 and intoxication < 0.05:
        return 1
    
    # Avoid beer unless alertness is critically low and no intoxication
    if alertness < 0.3 and intoxication < 0.02:
        return 2
    
    # Focus on working if all health metrics are well-balanced
    if alertness >= 0.6 and hypertension < 0.15 and intoxication < 0.05:
        return 0
    
    # Default to working with moderate risk if no clear health trigger
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)