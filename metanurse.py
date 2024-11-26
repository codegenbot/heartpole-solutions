import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if health indicators are poor
    if alertness < 0.4 or hypertension > 0.05 or intoxication > 0.05 or time_since_slept >= 4.0:
        return 3
    
    # Use coffee to boost alertness if not overly unhealthy
    if 0.4 <= alertness < 0.7 and hypertension < 0.04 and intoxication < 0.03:
        return 1
    
    # Safe to work if health indicators are stable
    if alertness >= 0.7 and hypertension < 0.03 and intoxication < 0.02:
        return 0
    
    # Resort to beer for stress relief if very low productivity and alertness
    if work_done < 0.01 and intoxication <= 0.02 and alertness < 0.3:
        return 2
    
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)