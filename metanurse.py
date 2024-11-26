import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep for serious health indicators
    if hypertension > 0.010 or intoxication > 0.025:
        return 3
    
    # Sleep for low alertness or if awake for a long time
    if alertness < 0.6 or time_since_slept > 2.0:
        return 3

    # Drink coffee to boost productivity safely
    if alertness < 0.7 and hypertension < 0.0075 and intoxication < 0.010:
        return 1

    # Avoid beer unless conditions are extremely balanced
    if 0.65 <= alertness < 0.75 and 0.0075 < hypertension <= 0.010 and intoxication < 0.020:
        return 2

    # Default to working if everything is in safe ranges
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)