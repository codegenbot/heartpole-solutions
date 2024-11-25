import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Improve alertness criteria for sleep
    if time_since_slept > 8 or alertness < 0.5:
        return 3

    # Stricter control for intoxication
    if intoxication >= 0.1:
        return 3

    # Adjust hypertension management
    if hypertension >= 0.05:
        return 3  # Choose sleep when hypertension is moderate

    # Enhance alertness for caffeine use
    if hypertension < 0.04 and alertness < 0.7:
        return 1  # Use coffee conservatively

    # Ideal productivity state
    if alertness >= 0.8:
        return 0  # Just work

    # Default to cautious productivity
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)