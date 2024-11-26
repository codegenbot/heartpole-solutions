import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if essential
    if alertness < 0.6 or time_since_slept > 8.0:
        return 3
    
    # Avoid severe hypertension or intoxication
    if hypertension > 0.08 or intoxication > 0.08:
        return 3
    
    # Use coffee more liberally while monitoring health metrics
    if alertness < 0.8 and hypertension <= 0.06:
        return 1
    
    # Allow use of beer if alertness is sufficiently high
    if alertness >= 0.75 and intoxication < 0.03:
        return 2

    # Default to working if everything is nominal
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)