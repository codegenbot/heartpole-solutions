import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if intoxicated or very long without sleep
    if intoxication > 0.15 or time_since_slept > 8:
        return 3  # Sleep

    # Encourage sleep if alertness is very low
    if alertness < 0.4:
        return 3  # Sleep

    # Use coffee to boost alertness, ensuring hypertension and intoxication levels are safe
    if 0.4 <= alertness < 0.6 and hypertension <= 0.3 and intoxication <= 0.08:
        return 1  # Drink coffee and work

    # Avoid beer due to negative health effects; consider sleep or coffee instead

    # Regular work if alertness is sufficient and health indicators are controlled
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)