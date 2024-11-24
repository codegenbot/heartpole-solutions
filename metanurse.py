import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate health-based response
    if hypertension > 0.7 or intoxication > 0.6:
        return 3  # Sleep to recover from high risk

    # Excessive time since sleep or low alertness
    if time_since_slept > 6 or alertness < 0.4:
        return 3  # Sleep

    # Coffee strategy for moderate alertness boost
    if alertness < 0.65 and hypertension < 0.4:
        return 1  # Drink coffee and work

    # Avoid beer unless alertness is critically low and health parameters are optimal
    if intoxication < 0.2 and hypertension < 0.25 and alertness < 0.5:
        return 2  # Drink beer and work

    # If conditions are optimal for work
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.3:
        return 0  # Just work

    # Default to sleep to prevent burnout
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)