import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Always prioritize health issues first
    if hypertension > 0.02 or intoxication > 0.07:
        return 3  # immediately sleep due to potentially serious health issues

    # Consider sleeping if sleep deprivation is becoming significant
    if time_since_slept >= 5:
        return 3  # sleep to avoid longer-term health impacts and maintain productivity

    # Drink coffee if productivity can be gained without significant health trade-offs
    if alertness < 0.5 and hypertension < 0.01 and intoxication < 0.02:
        return 1  # safely boost alertness with coffee

    # Opt for work when health metrics are optimal & alertness sufficient
    if alertness >= 0.6:
        return 0  # work normally
    
    # Default to sleeping when alertness is low and other factors don't strongly suggest coffee
    return 3  # otherwise, prioritize rest

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)