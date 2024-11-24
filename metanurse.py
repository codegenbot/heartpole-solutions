import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate health-based response
    if hypertension > 0.65 or intoxication > 0.5:
        return 3  # Sleep to recover from high-risk

    # Excessive time since sleep or low alertness
    if time_since_slept > 5 or alertness < 0.5:
        return 3  # Prefer Sleep

    # Coffee strategy for moderate alertness boost
    if alertness >= 0.5 and alertness < 0.7 and hypertension < 0.35:
        return 1  # Drink coffee and work

    # Work with optimal parameters
    if alertness >= 0.7 and hypertension < 0.35 and intoxication < 0.25:
        return 0  # Just work

    # Avoid beer unless all conditions are favorable
    if intoxication < 0.15 and hypertension < 0.2 and alertness < 0.4:
        return 2  # Drink beer and work

    # Default to sleep for safety when conditions are not optimal
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)