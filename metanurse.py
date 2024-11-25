import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Strictly avoid health risks
    if hypertension > 0.15 or intoxication > 0.15 or time_since_slept > 6:
        return 3  # sleep if any serious health issues
    
    # Ensure high alertness for maximum efficiency
    if alertness < 0.45:
        return 3  # sleep to recover alertness
    
    # Use coffee optimally for moderate alertness with minimal hypertension
    if alertness < 0.7:
        if hypertension < 0.1:
            return 1  # drink coffee if alertness is low and no severe conditions
    
    # Ensure conditions optimal for just working
    if alertness >= 0.75 and hypertension < 0.08 and intoxication < 0.04:
        return 0  # just work to maximize productivity
    
    # Use beer moderately when needed
    if work_done < 0.2 and alertness > 0.45:
        if intoxication < 0.07:  # ensure intoxication is low before taking beer
            return 2  # beer to relax and work if not overly intoxicated
    
    return 0  # default to just working if everything else is optimal

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)