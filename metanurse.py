import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleeping if any health condition is critical
    if alertness < 0.3 or time_since_slept >= 5 or intoxication > 0.10 or hypertension > 0.05:
        return 3  # Sleep
    # Drink coffee as a second choice to improve alertness
    if alertness < 0.5 and hypertension <= 0.03:
        return 1  # Drink coffee
    # Work when parameters are optimal
    if alertness >= 0.8 and intoxication < 0.05 and hypertension < 0.03:
        return 0  # Just work
    # Drink beer safely - cautious of intoxication and moderate hypertension
    if 0.5 <= alertness < 0.8 and intoxication < 0.08 and hypertension < 0.02:
        return 2  # Drink beer & work
    # Default to work if no conditions trigger other actions
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)