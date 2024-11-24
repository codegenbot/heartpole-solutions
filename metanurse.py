import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if serious enough indicator suggests health should be prioritized
    if alertness < 0.4 or hypertension > 0.6 or intoxication > 0.3 or time_since_slept >= 6:
        return 3  # Sleep
    
    # Coffee can help boost productivity slightly when alertness is moderate
    if alertness < 0.7 and hypertension <= 0.35 and intoxication <= 0.05:
        return 1  # Coffee and work

    # Just work if the conditions are generally safe
    if alertness >= 0.7 and hypertension <= 0.5 and intoxication <= 0.1:
        return 0  # Just work

    # If hypertension increases but intoxication is controllable; prioritize safer working condition
    if hypertension > 0.5 and intoxication < 0.15:
        return 2  # Drink beer and work

    return 0  # Default to just work when uncertain about increased risks

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)