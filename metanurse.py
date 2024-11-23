import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping if health indicators are risky
    if time_since_slept >= 8 or hypertension >= 0.3 or intoxication >= 0.3:
        return 3  # Sleep
    
    # Prefer sleep to enhance low alertness
    if alertness < 0.4:
        return 3  # Sleep
    
    # Use coffee to enhance mid-level alertness
    if alertness < 0.7:
        return 1  # Drink coffee and work
    
    # Avoid beer unless conditions are very favorable
    if intoxication < 0.2 and alertness >= 0.9:
        return 2  # Drink beer and work
    
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)