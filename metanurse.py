import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep immediately if high-risk health indicators are detected
    if hypertension > 0.012 or intoxication > 0.03:
        return 3
    
    # Sleep recommendation for low alertness or extended wakefulness
    if alertness < 0.65 or time_since_slept > 2.2:
        return 3

    # Use coffee if it can boost alertness safely
    if alertness < 0.75 and hypertension < 0.008 and intoxication < 0.015:
        return 1

    # Consider beer in a narrow range of balanced conditions
    if 0.65 <= alertness < 0.8 and 0.008 < hypertension <= 0.012 and intoxication < 0.025:
        return 2

    # Default to working if health indicators are within safe limits
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)