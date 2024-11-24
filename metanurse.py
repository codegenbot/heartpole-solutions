import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if too long since last sleep or unhealthy levels
    if time_since_slept > 8 or hypertension > 0.6 or intoxication >= 0.5:
        return 3  
    # Use coffee if alertness is low and hypertension and intoxication are controlled
    if alertness < 0.5 and hypertension <= 0.5 and intoxication < 0.3:
        return 1  
    # If alertness is sufficient, just work
    if alertness >= 0.5 and hypertension < 0.6 and intoxication < 0.4:
        return 0  
    # Use beer if it helps moderately without severe intoxication
    if intoxication < 0.5:
        return 2  
    # Default action if no other condition is met (not ideal but safe)
    return 0  

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)