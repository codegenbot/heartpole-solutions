import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if any health metric is critical
    if hypertension > 0.4 or intoxication > 0.3 or time_since_slept > 8:
        return 3  # Sleep

    # Sleep if alertness is particularly low
    if alertness < 0.5:
        return 3  # Sleep

    # Drink coffee if alertness is moderate, and health is stable
    if 0.5 <= alertness < 0.7 and hypertension <= 0.3 and intoxication <= 0.2:
        return 1  # Drink coffee and work

    # Drink beer if slightly intoxicated but alertness is still high
    if intoxication > 0.15 and alertness > 0.8:
        return 2  # Drink beer and work

    # Otherwise, default to just working
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)