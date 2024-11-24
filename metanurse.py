import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep to quickly reduce time_since_slept if it's very high
    if time_since_slept >= 6 or alertness < 0.3:
        return 3  # Sleep
    
    # Moderate caffeine consumption based on specific range
    if 0.4 <= alertness <= 0.7 and hypertension < 0.6 and intoxication < 0.3:
        return 1  # Drink coffee and work
    
    # Avoid any action when health conditions are risky
    if hypertension > 0.7 or intoxication > 0.5:
        return 3  # Sleep

    # Continue working when at optimal conditions
    if alertness > 0.75 and hypertension < 0.5 and intoxication < 0.25:
        return 0  # Just work

    # Default to sleeping if no clear action is suitable
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)