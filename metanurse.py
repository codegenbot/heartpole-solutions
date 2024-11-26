import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Handle serious health risks promptly
    if hypertension >= 0.12 or intoxication >= 0.3:
        return 3  # Sleep to mitigate health risks

    # Ensure adequate rest if alertness is low or enough time has passed
    if time_since_slept >= 5 or alertness < 0.5:
        return 3  # Sleep for necessary recovery

    # Drink coffee to improve alertness with safe health conditions
    if alertness < 0.8 and hypertension < 0.12 and intoxication < 0.3:
        return 1  # Drink coffee and continue working

    # Occasionally just work to avoid over-dependence on coffee
    if alertness >= 0.7:
        return 0  # Just work

    # Default to continue working if no conditions are urgent
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)