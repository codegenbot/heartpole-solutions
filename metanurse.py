import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep for critical health risk from hypertension or intoxication
    if hypertension > 0.03 or intoxication > 0.03:
        return 3

    # Sleep if alertness too low or slept too long ago 
    if alertness < 0.6 or time_since_slept > 5:
        return 3

    # Drink coffee if alertness is moderate but no immediate hypertension risk
    if 0.6 <= alertness < 0.8 and hypertension < 0.02:
        return 1

    # Just work if alertness is adequately high
    if alertness >= 0.9:
        return 0

    # Default to just work if no other conditions met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)