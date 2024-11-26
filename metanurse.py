import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if any health indicator is critical
    if alertness < 0.4 or hypertension >= 0.05 or intoxication >= 0.05 or time_since_slept >= 4.0:
        return 3
    
    # Safe to work if all health indicators are stable
    if alertness >= 0.7 and hypertension < 0.03 and intoxication < 0.02:
        return 0
    
    # Use coffee to boost alertness only if it can significantly help and you're not too unhealthy
    if 0.5 <= alertness < 0.7 and hypertension < 0.04 and intoxication < 0.03:
        return 1
    
    # Resort to beer only if alertness is critically low and no other option
    if alertness < 0.3 and work_done < 0.01 and intoxication < 0.02:
        return 2
    
    # Fallback to coffee if it's a safer option to try, else prioritize rest
    if alertness >= 0.4 and hypertension < 0.04 and intoxication < 0.03 and time_since_slept < 3.0:
        return 1
    
    return 3  # fallback to sleep if conditions are uncertain

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)