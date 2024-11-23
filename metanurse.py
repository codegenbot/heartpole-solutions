import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Health-first considerations
    if hypertension > 0.4 or intoxication > 0.3:
        return 3  # Prioritize sleep to recover from high hypertension or intoxication
    if time_since_slept > 12 or alertness < 0.4:
        return 3  # Sleep if it's been a long time or alertness is low

    # Caffeine boost only if reasonably safe
    if alertness < 0.5 and hypertension < 0.3:
        return 1  # Coffee can boost alertness safely

    # Avoid beer if intoxication is a concern
    if alertness < 0.5 and intoxication < 0.2:
        return 2  # Drink beer with caution

    # Favorable conditions for normal work
    if alertness >= 0.6 and hypertension <= 0.25 and intoxication <= 0.15:
        return 0  # Optimal work conditions
    
    # Default to working if no immediate issues
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)