import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if alertness is too low or too long since last sleep
    if alertness < 0.6 or time_since_slept > 6:
        return 3
      
    # Sleep if there are any signs of health risk from hypertension or intoxication
    if hypertension >= 0.07 or intoxication > 0.08:
        return 3

    # Drink coffee if alertness is low but not too low, and no hypertension
    if 0.6 <= alertness < 0.8 and hypertension < 0.03:
        return 1

    # Just work if alertness is high
    if alertness >= 0.8:
        return 0

    # Drink beer to relax if alertness is moderate and no health issues
    if alertness >= 0.7 and intoxication < 0.05:
        return 2

    return 2 # Default to a relaxed state with beer if no better action is found

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)