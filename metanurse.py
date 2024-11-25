import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if alertness is too low or time since last slept is high
    if alertness < 0.4 or time_since_slept > 6:
        return 3
    
    # Sleep if hypertension or intoxication are dangerously high
    if hypertension > 0.12 or intoxication > 0.1:
        return 3
    
    # Use coffee if alertness is moderately low, but overall health parameters are stable
    if alertness < 0.6 and hypertension < 0.1 and intoxication <= 0.03:
        return 1
        
    # Work if alertness is high and health parameters are well-controlled
    if alertness >= 0.6 and hypertension <= 0.08 and intoxication <= 0.02:
        return 0

    # Use beer as a last resort, when alertness is decent and work_done is low
    if alertness > 0.55 and work_done < 0.05:
        return 2

    # Default to safe option
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)