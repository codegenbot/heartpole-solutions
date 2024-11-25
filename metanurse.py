import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize resolving serious health issues
    if hypertension > 0.2 or intoxication > 0.2 or time_since_slept > 6:
        return 3  # sleep if any serious health issues
    
    # Ensure baseline alertness for working
    if alertness < 0.35:
        return 3  # sleep to recover alertness
    
    if alertness < 0.55:
        if hypertension < 0.15:  # avoid coffee if hypertension is relatively high
            return 1  # drink coffee if moderately alert and no severe conditions
    
    # Optimize conditions for working
    if alertness >= 0.7 and hypertension < 0.1 and intoxication < 0.05:
        return 0  # just work to maximize productivity
    
    # Provide moderate relaxation when needed
    if work_done < 0.25 and alertness > 0.4:
        if intoxication < 0.1:  # ensure intoxication is low before taking beer
            return 2  # beer to relax slightly and work
    
    return 0  # default to just working if everything else is optimal

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)