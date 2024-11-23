import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Stricter health risk thresholds
    if hypertension > 0.2 or intoxication > 0.1 or time_since_slept > 6:
        return 3  # Sleep

    # Sleep if alertness is critically low
    if alertness < 0.65:
        return 3  # Sleep

    # Coffee for moderate alertness if safe health parameters
    if 0.65 <= alertness < 0.8 and hypertension < 0.15 and intoxication < 0.08:
        return 1  # Drink coffee and work

    # Regular sleep intervals to ensure productivity balance
    if time_elapsed % 150 == 0:
        return 3  # Periodic rest every 150 steps

    # Default work condition
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)