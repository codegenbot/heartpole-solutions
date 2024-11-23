import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Health-first considerations
    if hypertension > 0.5 or intoxication > 0.4:
        return 3  # Sleep to reduce hypertension/intoxication more aggressively
    if time_since_slept > 14 or alertness < 0.3:
        return 3  # Critical need for sleep to improve alertness
    
    # Use coffee to maintain alertness without high hypertension
    if alertness < 0.5 and hypertension < 0.35:
        return 1  # Drink coffee and work to boost alertness
    
    # Avoid beer if intoxication is a concern, unless alertness is too low
    if alertness < 0.4 and intoxication < 0.3:
        return 2  # Drink beer and work only if it's safe
    
    # Favorable conditions for normal work
    if alertness >= 0.6 and hypertension <= 0.25 and intoxication <= 0.15:
        return 0  # Continue working under optimal conditions
    
    # Default to working if no immediate issues
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)