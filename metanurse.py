import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if any health risk is detected more aggressively
    if alertness < 0.5 or hypertension > 0.12 or intoxication > 0.08 or time_since_slept > 6:
        return 3
    
    # Allow coffee when alertness is low and conditions are safer
    if alertness < 0.6 and hypertension < 0.09 and intoxication < 0.02 and time_since_slept < 5:
        return 1

    # Work when sufficient alertness and safe health stats
    if alertness >= 0.6 and hypertension <= 0.09 and intoxication <= 0.02:
        return 0
    
    # Use beer conservatively when productivity and conditions are right
    if work_done < 0.2 and alertness > 0.6 and hypertension < 0.07 and intoxication < 0.01:
        return 2

    # Default action if none conditions are fully met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)