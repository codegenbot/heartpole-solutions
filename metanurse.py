import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Strongly prioritize sleep if any critical metric suggests fatigue or health risk
    if alertness <= 0.7 or hypertension > 0.25 or intoxication > 0.12 or time_since_slept >= 7:
        return 3  # Sleep to recover
    
    # Lower usage of coffee, only when alertness is low but hypertension and intoxication are safe
    if alertness < 0.8 and hypertension < 0.15 and intoxication < 0.1 and time_since_slept < 6:
        return 1  # Use coffee cautiously
    
    # Rarely allow beer, only when fully alert and safe
    if alertness == 1.0 and intoxication <= 0.02 and hypertension < 0.05:
        return 2  # Beer only for negligible and safe conditions
    
    return 0  # Just work if everything is controlled

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)