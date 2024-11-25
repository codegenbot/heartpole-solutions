import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Major health priorities
    if hypertension > 0.15 or intoxication > 0.1 or time_since_slept > 5:
        return 3  # prioritize sleeping to address these issues

    # Alertness management
    if alertness < 0.5:
        return 3  # sleep to regain minimal alertness
    
    if alertness < 0.7:
        if hypertension < 0.1:
            return 1  # coffee to boost alertness without risking hypertension
    
    # Productive working conditions
    if alertness >= 0.8 and hypertension < 0.05 and intoxication < 0.02:
        return 0  # maximum productivity conditions met
    
    # Moderate relaxation
    if work_done < 0.3 and alertness > 0.6:
        if intoxication < 0.07:
            return 2  # relax while intoxication risk is minimal and work when relaxed
    
    return 0  # default to work if conditions are generally favorable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)