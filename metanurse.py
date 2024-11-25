import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if alertness is extremely low, hypertension is dangerously high, or too much time has passed without sleep
    if alertness < 0.4 or hypertension > 0.12 or intoxication > 0.09 or time_since_slept > 6:
        return 3
    
    # Use coffee if alertness is moderate and health parameters are within safe limits
    if alertness < 0.6 and hypertension < 0.09 and intoxication < 0.03 and time_since_slept <= 4:
        return 1
    
    # Prefer working if all parameters are in optimal range
    if alertness >= 0.6 and hypertension <= 0.08 and intoxication <= 0.03 and time_since_slept <= 5:
        return 0
    
    # Opt for beer under relaxed conditions if work is significantly behind
    if work_done < 0.15 and alertness > 0.5 and hypertension < 0.07 and intoxication < 0.02:
        return 2

    # Default action to maintain productivity
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)