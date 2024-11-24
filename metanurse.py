import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for serious indicators, slightly more cautious
    if alertness < 0.5 or hypertension > 0.65 or intoxication > 0.25 or time_since_slept >= 5:
        return 3  # Sleep
        
    # Leverage coffee prudently for moderate alertness, safer thresholds
    if alertness < 0.75 and hypertension <= 0.4 and intoxication <= 0.05:
        return 1  # Coffee and work
        
    # Opt to work under generally safe conditions
    if alertness >= 0.75 and hypertension <= 0.55 and intoxication <= 0.1:
        return 0  # Just work

    # Reduce reliance on beer; avoid when hypertension is a concern
    if intoxication <= 0.1:
        return 0  # Default to just work when no other context suggests a better approach

    return 0  # Default to just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)