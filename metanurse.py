import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if alertness is critically low or other serious health conditions occur
    if alertness < 0.2 or hypertension > 0.9 or intoxication > 0.7:
        return 3

    # Just work if alertness is very high and health conditions are optimal
    if alertness > 0.9 and hypertension < 0.6 and intoxication < 0.2:
        return 0

    # Use coffee to maintain or boost alertness if hypertension and intoxication allow
    if 0.3 <= alertness <= 0.8 and hypertension < 0.7 and intoxication < 0.3:
        return 1

    # Drink beer if intoxication is low and alertness is decreasing, but hypertension is controlled
    if alertness < 0.3 and hypertension < 0.6 and intoxication < 0.3:
        return 2

    # Return to sleep if other conditions suggest it's the safe fallback
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)