import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health metrics first
    if hypertension > 0.06 or intoxication > 0.12:
        return 3  # Sleep if any health metric is too high
    
    if time_since_slept > 8:
        return 3  # Sleep if it's been too long since last sleep

    # Encourage working with higher alertness and safe health metrics
    if alertness >= 0.7 and hypertension < 0.04 and intoxication < 0.04:
        return 0  # Just work

    # Use coffee or beer based on alertness but ensure health safety
    if alertness < 0.55 and hypertension < 0.05 and intoxication < 0.05:
        return 1  # Drink coffee and work

    if alertness < 0.45 and intoxication < 0.09:
        return 2  # Drink beer and work

    return 3  # Default is to sleep as a preventive measure

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)