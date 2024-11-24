import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Always prioritize sleep if health indicators are very high
    if hypertension > 0.6 or intoxication > 0.4 or time_since_slept > 10:
        return 3  # Sleep

    # Ensure moderate rest to prevent high risks before they manifest
    if 7 <= time_since_slept <= 10 and (hypertension > 0.5 or intoxication > 0.3):
        return 3  # Sleep

    # Utilize coffee only when it's likely to have a tangible positive effect
    if alertness < 0.5 and hypertension < 0.4 and intoxication < 0.3:
        return 1  # Drink coffee and work

    # Prioritize working without additional stimuli if alertness is optimal
    if 0.6 <= alertness <= 0.9 and hypertension < 0.4 and intoxication < 0.3:
        return 0  # Just work

    # If minor alertness drop but otherwise stable, consider minor intoxication
    if 0.5 <= alertness < 0.6 and hypertension < 0.3 and intoxication < 0.2:
        return 1  # Drink coffee and work
    
    # Final safeguard to ensure work doesn't overstrain the person
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)