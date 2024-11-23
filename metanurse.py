import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Critical conditions requiring sleep
    if hypertension > 0.7 or intoxication > 0.5 or alertness < 0.2 or time_since_slept >= 16:
        return 3
    
    # Prefer work under very good conditions
    if alertness >= 0.9 and hypertension <= 0.3 and intoxication == 0.0:
        return 0
    
    # Coffee in moderation for low alertness and low hypertension
    if alertness < 0.5 and hypertension <= 0.4:
        return 1

    # Beer to relieve stress (hypertension) when intoxication is manageable
    if hypertension > 0.4 and intoxication < 0.3:
        return 2

    # Sleep as a fallback when moderately stressed
    if alertness < 0.3 or time_since_slept > 14:
        return 3

    # Default to work if balanced
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)