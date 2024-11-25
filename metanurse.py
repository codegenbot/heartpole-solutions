import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep with more balanced thresholds
    if alertness < 0.3 or time_since_slept > 8 or hypertension > 0.6:
        return 3  # Sleep

    # Allow more flexibility for just working if indicators are within acceptable ranges
    if alertness >= 0.65 and hypertension <= 0.4 and intoxication <= 0.07:
        return 0  # Just work

    # Use coffee to boost productivity while keeping under a health-safe threshold
    if 0.5 <= alertness < 0.65 and hypertension <= 0.45 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # If productivity is low and needing improvement, opt for beer as a last resort
    if work_done < 0.5 and intoxication < 0.3:
        return 2  # Drink beer and work
    
    return 3  # Defaulting to sleep if no criteria match

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)