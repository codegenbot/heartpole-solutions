import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep for critical health risk from hypertension or intoxication
    if hypertension > 0.07 or intoxication > 0.07:
        return 3

    # Sleep if alertness too low or slept too long ago
    if alertness < 0.4 or time_since_slept > 5:
        return 3

    # Drink coffee if alertness is low but no immediate hypertension risk
    if 0.4 <= alertness < 0.6 and hypertension < 0.04:
        return 1

    # Just work if alertness is adequately high
    if alertness >= 0.75:
        return 0

    # Default to a relaxed state with beer if no better action is found
    return 2 

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)