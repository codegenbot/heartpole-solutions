import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Always prioritize sleep if health metrics are critical
    if alertness < 0.5 or hypertension > 0.6 or intoxication > 0.15 or time_since_slept > 10:
        return 3  # Sleep

    # Work optimally when all parameters are well-balanced
    if alertness >= 0.7 and hypertension <= 0.35 and intoxication <= 0.05:
        return 0  # Just work

    # Use coffee when slightly low alertness, but consider risks
    if 0.5 <= alertness < 0.7 and hypertension <= 0.4 and intoxication < 0.1:
        return 1  # Drink coffee and work

    # Resort to beer sparingly under moderate conditions
    if alertness <= 0.6 and intoxication < 0.1:
        return 2  # Drink beer and work

    # Generally sleep if more than 7 hours since last rest
    if time_since_slept > 7:
        return 3  # Sleep
    
    # Default to work if conditions are ambiguous
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)