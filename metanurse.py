import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if any immediate health issue thresholds are met
    if hypertension > 0.6 or intoxication > 0.5 or alertness < 0.2 or time_since_slept > 16:
        return 3
    
    # Use coffee when alertness is low, ensuring hypertension is low
    if alertness < 0.5 and hypertension <= 0.4:
        return 1
    
    # Use beer only if alertness is low and intoxication is negligible
    if alertness < 0.4 and intoxication < 0.02:
        return 2
    
    # Only work directly if health metrics are optimal
    if alertness >= 0.8 and hypertension <= 0.25 and intoxication <= 0.05:
        return 0
    
    # Promote sleep to avoid long awake periods if no optimal work conditions exist
    if time_since_slept > 14:
        return 3

    # Default to working to maximize productivity
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)