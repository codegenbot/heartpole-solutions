import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if any health metric is critical
    if hypertension > 0.35 or intoxication > 0.25 or time_since_slept > 7:
        return 3  # Sleep

    # Sleep if alertness is low
    if alertness < 0.6:
        return 3  # Sleep

    # Avoid all caffeinated or alcohol actions if intoxication or hypertension is moderate
    if 0.3 <= hypertension <= 0.4 or 0.2 <= intoxication <= 0.3:
        return 0  # Just work to stabilize

    # Drink coffee if alertness is moderate, and health is very stable
    if 0.6 <= alertness < 0.8 and hypertension <= 0.3 and intoxication <= 0.15:
        return 1  # Drink coffee and work

    # Drink beer if slightly intoxicated but alertness is still very high
    if intoxication > 0.1 and alertness > 0.75:
        return 2  # Drink beer and work

    # Otherwise, default to just working
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)