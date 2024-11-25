import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if low alertness or long time since sleep
    if alertness < 0.5 or time_since_slept > 7:
        return 3

    # Avoid caffeine if notable hypertension; prioritize body rest instead
    if hypertension >= 0.05:
        return 3 if alertness < 0.75 else 0

    # Avoid work if high intoxication; offer sleep more cautiously
    if intoxication > 0.1:
        return 3

    # Strategize caffeine consumption for optimal productivity
    if alertness < 0.65 and hypertension < 0.03:
        return 1

    # Optimal alertness for productive work
    if alertness >= 0.7:
        return 0

    # Default to cautious work strategy
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)