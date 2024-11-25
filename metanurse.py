import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep for critical health risk from hypertension or intoxication
    if hypertension > 0.05 or intoxication > 0.05:
        return 3

    # Sleep if alertness too low or slept too long ago 
    if alertness < 0.5 or time_since_slept > 6:
        return 3

    # Drink coffee if alertness is low but no immediate hypertension risk
    if 0.5 <= alertness < 0.7 and hypertension < 0.03:
        return 1

    # Just work if alertness is adequately high
    if alertness >= 0.8:
        return 0

    # Default to a relaxed state with beer if no better action is found
    return 2 

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)