import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep to maintain alertness and manage time since last slept
    if time_since_slept > 10 or alertness < 0.3:
        return 3

    # Avoid work if intoxication is dangerously high
    if intoxication >= 0.15:
        return 3

    # Manage hypertension effectively
    if hypertension >= 0.07 and alertness < 0.5:
        return 3
    if hypertension < 0.05 and alertness < 0.6:
        return 1  # Use coffee for slight alertness boost where hypertension is low

    # Ideal productivity state
    if alertness >= 0.7:
        return 0  # Just work

    # Default to cautious productivity
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)