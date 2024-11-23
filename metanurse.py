import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Intoxication and rest
    if intoxication > 0.3 or time_since_slept > 7:
        return 3
    # High hypertension requires rest
    if hypertension > 0.7:
        return 3
    # If moderately hypertensive, avoid caffeine
    if hypertension > 0.5 and work_done > 5:
        return 3
    # Manage alertness
    if alertness < 0.3:
        if time_since_slept > 4:
            return 3
        else:
            return 1
    # Work if alertness is high and intoxication low
    if alertness > 0.7 and intoxication < 0.2:
        return 0
    # Default moderate action
    return 1

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)