import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.7 or intoxication > 0.8 or time_since_slept > 6:
        return 3  # Prioritize sleep if health is at risk
    if alertness < 0.2:
        return 1  # Drink coffee to boost alertness when it's critically low
    if intoxication > 0.5 and alertness < 0.5:
        return 2  # Drink beer, intoxication outweighs productivity
    if alertness > 0.75 and hypertension < 0.3 and intoxication < 0.3:
        return 0  # Safe to work in an optimal state
    return 0  # Default to work when conditions are balanced

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)