import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for health critical states
    if hypertension > 0.20 or intoxication > 0.05 or time_since_slept > 5:
        return 3  # Sleep

    # Sleep when alertness is too low
    if alertness < 0.6:
        return 3  # Sleep

    # Drink coffee if alertness is low but health indicators are under control
    if 0.6 <= alertness < 0.75 and hypertension <= 0.10 and intoxication <= 0.02:
        return 1  # Drink coffee and work

    # In safer conditions, drink beer if alertness is slightly low
    if 0.75 <= alertness < 0.8 and hypertension <= 0.10 and intoxication < 0.05:
        return 2  # Drink beer and work

    # Just work when conditions are optimal
    return 0  # Just work

# Loop through input
for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)