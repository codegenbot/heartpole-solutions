import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.5 or intoxication > 0.3 or time_since_slept > 5:
        return 3  # Sleep
    if alertness < 0.6 and hypertension < 0.35 and intoxication < 0.2:
        return 1  # Drink coffee and work
    if alertness >= 0.75 and hypertension < 0.45 and intoxication < 0.15:
        return 0  # Just work
    if alertness >= 0.6 and hypertension < 0.4 and intoxication < 0.1:
        return 2  # Drink beer and work
    return 3  # Default to sleeping for better recovery    

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)