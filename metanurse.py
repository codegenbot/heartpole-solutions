import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize health by resting if hypertension or intoxication are beyond safe limits
    if hypertension > 0.25 or intoxication > 0.15:
        return 3

    # Prioritize sleep if alertness is very low or it's been a long time since last sleep
    if alertness < 0.5 or time_since_slept > 16:
        return 3

    # Use coffee to boost productivity when fatigue is mild and safe health parameters
    if alertness < 0.7 and hypertension <= 0.15 and intoxication <= 0.05:
        return 1
    
    # Encourage relaxation with beer if stress-related parameters are fine
    if alertness >= 0.9 and hypertension <= 0.1 and intoxication <= 0.05:
        return 2

    # Default to just working when conditions are optimal
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)