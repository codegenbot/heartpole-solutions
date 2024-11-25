import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if low alertness or long time since sleep
    if alertness < 0.6 or time_since_slept > 6:
        return 3

    # Avoid caffeine if there's any notable hypertension
    if hypertension >= 0.06:
        return 3 if alertness < 0.7 else 0

    # Avoid work if any intoxication level is present
    if intoxication > 0:
        return 3

    # Strategize caffeine consumption for optimal productivity
    if alertness < 0.7 and hypertension < 0.04:
        return 1

    # Optimal alertness for productive work
    if alertness >= 0.7:
        return 0

    # Default to cautious work strategy
    return 2 if alertness < 0.65 else 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)