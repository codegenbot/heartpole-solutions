import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Priority for resting, especially if alertness is low or time since last sleep > 6 hours
    if alertness < 0.6 or time_since_slept > 6:
        return 3  # Sleep
    
    # If well-rested and low on hypertension/intoxication, just work
    if alertness >= 0.8 and hypertension < 0.3 and intoxication < 0.1:
        return 0  # Just work

    # If moderate alertness and safe levels of hypertension/intoxication, use coffee responsibly
    if 0.6 <= alertness < 0.8 and hypertension < 0.4 and intoxication < 0.1:
        return 1  # Drink coffee and work

    # If needing mild relaxation and safe levels, consider beer
    if intoxication < 0.05 and hypertension < 0.3:
        return 2  # Drink beer and work

    # Default to just work when in doubt
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)