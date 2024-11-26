import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Handle serious health risks promptly
    if hypertension >= 0.15 or intoxication >= 0.35:
        return 3  # Sleep to mitigate health risks

    # Ensure adequate rest if alertness is low or enough time has passed
    if time_since_slept >= 6 or alertness < 0.4:
        return 3  # Sleep for necessary recovery

    # Only drink coffee if it will be effective without severe health risks
    if alertness < 0.7 and hypertension < 0.15 and intoxication < 0.35:
        return 1  # Drink coffee and continue working

    # If none of the above conditions demand intervention, continue working
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)