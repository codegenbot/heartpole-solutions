import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate response to critical health metrics
    if hypertension > 0.2 or intoxication > 0.2 or time_since_slept > 7:
        return 3  # sleep to tackle serious issues
    
    # Sleep if severely lacking alertness
    if alertness < 0.5:
        return 3

    # Use coffee only if safe from high hypertension
    if alertness < 0.7 and hypertension < 0.15:
        return 1  # moderate boost in alertness without coffee dependency
    
    # Ideal working conditions
    if alertness >= 0.8 and hypertension < 0.1 and intoxication < 0.05:
        return 0  # continue working efficiently
    
    # Relax conditionally when workload is lower
    if work_done < 0.4 and intoxication < 0.1:
        return 2  # mild relaxation with beer
    
    return 0  # default to just work when conditions are stable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)