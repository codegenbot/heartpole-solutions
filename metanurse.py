import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediately address critical health concerns
    if time_since_slept >= 6 or alertness < 0.3:
        return 3  # Sleep immediately if very deprived

    # High hypertension overrules other actions when health is threatened
    if hypertension > 0.8 and intoxication < 0.1:
        return 2  # Drink beer and work carefully

    # Moderate alertness issue with safe health values to use coffee
    if alertness < 0.5 and hypertension < 0.6 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Optimal productivity without any interference in health
    if alertness >= 0.75 and hypertension <= 0.4 and intoxication <= 0.1:
        return 0  # Just work
    
    # Fall back on improving health with beer work mix in moderate conditions
    if hypertension > 0.5 and intoxication < 0.2:
        return 2  # Drink beer and work

    return 3  # Default to sleep if conditions are not optimum

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)