import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if severely intoxicated or haven't slept for long
    if intoxication > 0.4 or time_since_slept > 8:
        return 3
    # Hypertension is critical; rest if high
    if hypertension > 0.7:
        return 3
    # Balance rest and alertness
    if alertness < 0.3:
        if time_since_slept > 4:
            return 3
        else:
            return 1
    # Default actions
    if alertness > 0.7 and intoxication < 0.2:
        return 0  # Just work
    return 1  # Drink coffee and work for moderate alertness

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)