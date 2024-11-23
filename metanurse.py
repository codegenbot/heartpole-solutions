import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Enforce sleep if any health risk parameters exceed safe lower thresholds
    if hypertension > 0.30 or intoxication > 0.15 or time_since_slept > 8:
        return 3  # Sleep

    # Sleep if alertness is critically low
    if alertness < 0.6:
        return 3  # Sleep

    # Consider drinking coffee based on specific conditions to improve alertness
    if 0.6 <= alertness < 0.75 and hypertension <= 0.2 and intoxication <= 0.1:
        return 1  # Drink coffee and work

    # Default to working if vital signs are within the healthiest range
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)