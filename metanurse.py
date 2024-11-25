import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize resolving serious health issues
    if hypertension > 0.15 or intoxication > 0.10 or time_since_slept > 5:
        return 3  # lower thresholds for sleep due to health issues
    
    # Adjust alertness criteria
    if alertness < 0.4:
        return 3  # sleep to recover alertness when very low
    
    if alertness < 0.6:
        if hypertension < 0.10:
            return 1  # use coffee cautiously when alertness is moderate

    # Optimize conditions for working with balanced thresholds
    if alertness >= 0.8 and hypertension < 0.06 and intoxication < 0.02:
        return 0  # prioritize working under very optimal conditions
    
    # Adjust criteria for relaxation
    if work_done < 0.2 and alertness > 0.5:
        if intoxication < 0.05:  # stricter condition for beer
            return 2  # beer for slight relaxation and productivity boost

    return 0  # default to working if no other action is clearly necessary

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)