import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if conditions indicate poor health or exhaustion
    if alertness < 0.3 or hypertension > 0.25 or intoxication > 0.2 or time_since_slept > 12:
        return 3
    
    # If alertness is slightly low and other conditions are fine, consider coffee
    if alertness < 0.5 and hypertension <= 0.15 and intoxication < 0.1:
        return 1

    # Prioritize work when conditions are optimal
    if alertness >= 0.7 and hypertension <= 0.15 and intoxication <= 0.05:
        return 0

    # Use beer as a last resort if something to relax is needed but work is still possible
    if alertness >= 0.4 and work_done < 0.5:
        return 2

    # Default to normal work if no other priority
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)