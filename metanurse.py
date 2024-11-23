import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if highly intoxicated or very long without sleep
    if hypertension > 0.35 or intoxication > 0.2 or time_since_slept > 7:
        return 3  # Sleep

    # Encourage sleep if alertness drops significantly
    if alertness < 0.5:
        return 3  # Sleep

    # Use coffee if alertness is low while maintaining safe hypertension and intoxication levels
    if 0.5 <= alertness < 0.65 and hypertension <= 0.25 and intoxication <= 0.1:
        return 1  # Drink coffee and work

    # Consider using beer if there's mild intoxication
    if 0.5 <= alertness < 0.6 and 0.1 < intoxication <= 0.12:
        return 2  # Drink beer and work

    # Regular work if everything is in a good balance
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)