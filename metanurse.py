import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate response to critical health metrics
    if intoxication > 0.2 or hypertension > 0.15 or time_since_slept > 7:
        return 3  # sleep to tackle serious health issues
    
    # Prioritize sleep if very low alertness or adequate rest is not received
    if alertness < 0.4 or time_since_slept > 6:
        return 3

    # Use coffee to boost alertness safely
    if alertness < 0.6 and hypertension < 0.1:
        return 1  # safe moderate boost in alertness
    
    # Ideal working conditions
    if alertness >= 0.7 and hypertension < 0.1 and intoxication < 0.05:
        return 0  # continue working efficiently
    
    # Avoid using beer excessively
    if work_done < 0.5 and intoxication < 0.05:
        return 2  # mild relaxation with beer if conditions are safe
    
    return 0  # default to just work under stable conditions

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)