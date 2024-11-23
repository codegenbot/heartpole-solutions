import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep based on health conditions first
    if hypertension >= 0.35 or intoxication >= 0.3 or time_since_slept >= 5:
        return 3  # Sleep

    # Coffee to boost productivity when alertness is moderate and safe
    if 0.5 <= alertness < 0.7 and hypertension < 0.25 and intoxication < 0.1:
        return 1  # Drink coffee and work

    # To stabilize, sleep if alertness too low or sufficient time_without_sleep
    if alertness < 0.5 or time_since_slept >= 6:
        return 3  # Sleep

    # Working state when health risks are low 
    if alertness >= 0.7 and hypertension < 0.2 and intoxication < 0.1:
        return 0  # Just work

    # Avoid beer unless certain conditions met
    if 0.6 <= alertness < 0.75 and intoxication < 0.05:
        return 2  # Drink beer and work
    
    # Default action
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)