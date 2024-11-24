import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Higher priority for sleep to ensure recovery
    if alertness < 0.6 or time_since_slept > 6:
        return 3  # Sleep for recovery

    # Stricter conditions for health risks
    if hypertension > 0.3 or intoxication > 0.3:
        return 3  # Sleep to mitigate health issues

    # Use coffee only if health permits
    if alertness < 0.75 and hypertension < 0.25 and intoxication < 0.3:
        return 1  # Drink coffee to boost alertness

    # Pure work in optimal conditions
    if alertness >= 0.75 and hypertension < 0.3 and intoxication < 0.2:
        return 0  # Work

    # Further restrict beer usage
    if 0.25 <= hypertension < 0.4 and intoxication < 0.15:
        return 2  # Drink beer to relax

    # Default safe action
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)