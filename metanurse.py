import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if severely intoxicated or haven't slept for long or high hypertension
    if intoxication > 0.4 or time_since_slept > 8 or hypertension > 0.7:
        return 3
    # Prioritize sleep if alertness is below threshold, but consider work urgency
    if alertness < 0.3:
        return 3 if time_since_slept > 4 or work_done < (0.5 * time_elapsed) else 1
    # Perform actions based on alertness
    if alertness > 0.7:
        return 0 if intoxication < 0.2 else (2 if intoxication > 0.3 else 1)
    return 1  # Drink coffee and work for moderate alertness

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)