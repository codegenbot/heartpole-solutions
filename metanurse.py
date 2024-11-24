import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Always prioritize sleeping if health is clearly at risk
    if time_since_slept > 8 or hypertension > 0.35 or intoxication > 0.3:
        return 3
    # If alertness is low and hypertension is not too high, drink coffee
    if alertness < 0.6 and hypertension < 0.25:
        return 1
    # Avoid beer if already intoxicated, and only use if alertness is low
    if intoxication < 0.2 and alertness < 0.6:
        return 2
    # Work if conditions seem reasonably balanced
    if alertness >= 0.7 and hypertension < 0.2 and intoxication < 0.2:
        return 0
    # Default to sleep if no other condition is met to reset health parameters
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)