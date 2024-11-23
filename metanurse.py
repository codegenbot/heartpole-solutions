import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep on slightly lower thresholds
    if hypertension > 0.65 or intoxication > 0.45 or alertness < 0.15 or time_since_slept > 16:
        return 3
    
    # High alertness and low stress conditions - work directly
    if alertness >= 0.75 and hypertension <= 0.25 and intoxication <= 0.05:
        return 0
    
    # Consider sleep if moderately low alertness and extended awake time
    if alertness < 0.3 or time_since_slept > 12:
        return 3
    
    # Use coffee judiciously with lower hypertension tolerance
    if 0.3 <= alertness < 0.5 and hypertension <= 0.4:
        return 1
    
    # Be very cautious with beer use, only if intoxication is zero
    if 0.25 <= alertness < 0.4 and intoxication < 0.005:
        return 2

    # Default to working if not immediately at risk
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)