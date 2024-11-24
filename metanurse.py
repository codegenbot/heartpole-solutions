import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Always prioritize sleep if needed
    if time_since_slept > 8 or alertness < 0.4 or hypertension > 0.75 or intoxication > 0.5:
        return 3  # Sleep
    # Safe state for working hard
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.2:
        return 0  # Just work
    # Drink coffee if alertness is moderately low and risks are low
    if alertness < 0.6 and time_since_slept < 7 and hypertension < 0.5:
        return 1  # Drink coffee and work
    # Drink beer if slight relaxation is needed without over-indulgence
    if alertness < 0.5 and intoxication < 0.3 and hypertension < 0.5 and time_since_slept < 6:
        return 2  # Drink beer and work
    return 3  # Default to sleep as safe fallback

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)