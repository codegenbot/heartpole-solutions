import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping if significantly sleep-deprived or there's a health risk
    if time_since_slept > 6 or alertness < 0.3 or hypertension > 0.7:
        return 3  # Sleep to recuperate health
    # If alertness is low and can be boosted, use coffee
    if alertness < 0.6 and intoxication < 0.2 and hypertension <= 0.5:
        return 1  # Drink coffee and work
    # If intoxicated, attempt recovery
    if intoxication >= 0.2:
        return 3  # Sleep to potentially reduce intoxication
    # Optimal conditions for working
    if alertness >= 0.7 and hypertension < 0.5 and intoxication < 0.1:
        return 0  # Just work
    # Default to just working if no other conditions are triggered
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)