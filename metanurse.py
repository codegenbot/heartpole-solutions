import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if severely intoxicated, haven't slept for long or high hypertension
    if intoxication > 0.4 or time_since_slept > 8 or hypertension > 0.7:
        return 3
    # Prioritize sleep if alertness is low and work done isn't sufficient
    if alertness < 0.3:
        return 3 if time_since_slept > 4 or work_done < (0.5 * time_elapsed) else 1
    # High alertness actions
    if alertness > 0.7:
        return 0 if intoxication < 0.2 else (2 if intoxication > 0.3 else 1)
    # Default action for moderate alertness
    return 1

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)