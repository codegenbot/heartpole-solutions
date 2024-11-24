import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize critical health recovery: sleep if critical conditions are met
    if alertness < 0.5 or hypertension > 0.7 or intoxication > 0.35 or time_since_slept >= 5:
        return 3  # Sleep
    
    # Use caffeine judiciously under controlled conditions
    if alertness < 0.75 and hypertension < 0.4 and intoxication <= 0.1:
        return 1  # Coffee and work

    # Work optimally without stimulants
    if alertness >= 0.75 and hypertension <= 0.5 and intoxication <= 0.15:
        return 0  # Just work

    # Manage hypertension via beer cautiously
    if intoxication <= 0.2 and hypertension > 0.5:
        return 2  # Drink beer and work

    return 3  # Default to sleep if uncertain

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)