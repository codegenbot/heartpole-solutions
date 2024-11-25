import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if alertness is critically low or time since last sleep is excessive
    if alertness < 0.3 or time_since_slept > 8:
        return 3  # Sleep
    
    # Use coffee cautiously when alertness is moderately low and health is stable
    if 0.3 <= alertness <= 0.5 and hypertension < 0.4 and intoxication < 0.1:
        return 1  # Drink coffee and work

    # Ideal condition to just work
    if alertness > 0.7 and hypertension < 0.3 and intoxication < 0.15:
        return 0  # Just work

    # Restrict beer use unless mildly low alertness and healthy stability
    if 0.5 < alertness <= 0.6 and intoxication <= 0.05 and hypertension < 0.35:
        return 2  # Drink beer and work

    # Default to just work if no action is immediately clear
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)