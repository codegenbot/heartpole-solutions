import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize immediate sleep if any prudent health condition indicates
    if alertness < 0.5 or hypertension > 0.6 or intoxication >= 0.3 or time_since_slept > 5:
        return 3  # Prioritize sleep if feeling unwell
    
    # Use coffee for moderate alertness level without risking hypertension
    if 0.5 <= alertness < 0.7 and hypertension < 0.5 and intoxication <= 0.25:
        return 1  # Drink coffee and work

    # Opt for just working if alertness is high and health is in good standing
    if alertness >= 0.7 and hypertension <= 0.4 and intoxication < 0.2:
        return 0  # Just work

    # Avoid beer mostly, use only in specific relaxed scenarios
    if intoxication < 0.2 and hypertension < 0.4:
        return 2  # Drink beer and work

    return 3  # Default to sleep if no other option feels safe

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)