import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Critical health conditions must be addressed first
    if time_since_slept >= 6 or alertness < 0.5 or hypertension > 0.8 or intoxication > 0.5:
        return 3  # Sleep

    # Promote alertness safely by using coffee in mild conditions
    if alertness < 0.7 and hypertension < 0.6 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Manage hypertension with beer if intoxication is low
    if hypertension > 0.6 and intoxication < 0.3:
        return 2  # Drink beer and work

    # Maintain a productive state
    if alertness > 0.8 and hypertension < 0.5 and intoxication < 0.1:
        return 0  # Just work

    return 0  # Default to work in balanced conditions

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)