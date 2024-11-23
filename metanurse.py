import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate high-risk conditions - prioritize sleep
    if hypertension > 0.7 or intoxication > 0.5 or alertness < 0.1 or time_since_slept > 18:
        return 3
    
    # High alertness and low stress conditions - work directly
    if alertness >= 0.75 and hypertension <= 0.3 and intoxication <= 0.1:
        return 0
    
    # Consider sleep if moderately low alertness and extended awake time
    if alertness < 0.25 or time_since_slept > 14:
        return 3
    
    # Use coffee to boost moderate alertness if hypertension allows
    if alertness < 0.5 and hypertension <= 0.6:
        return 1
    
    # Use beer very cautiously, only if intoxication is zero
    if alertness < 0.4 and intoxication < 0.01:
        return 2

    # Default to working if no urgent health issues
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)