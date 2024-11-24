import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize Sleep if low alertness, high health risk indicators or long time awake
    if time_since_slept > 6 or alertness < 0.3 or hypertension > 0.6 or intoxication > 0.5:
        return 3  # Sleep

    # Encourage coffee consumption when alertness is low but health metrics are safe 
    if alertness < 0.6 and hypertension < 0.4 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Encourage just work when safe
    if alertness >= 0.6 and hypertension < 0.4 and intoxication < 0.2:
        return 0  # Just work
    
    # Avoid beer if intoxication is high; use it only when alertness can drop and it's safe
    if alertness < 0.5 and intoxication < 0.5 and hypertension < 0.5:
        return 2  # Drink beer and work
    
    # Default to sleep under uncertain or unsafe conditions
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)