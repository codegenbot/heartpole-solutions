import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if high hypertension, intoxication or excessive sleeplessness
    if hypertension > 0.30 or intoxication > 0.15 or time_since_slept > 6:
        return 3  # Sleep

    # Sleep if alertness is critically low, prior to health complications
    if alertness < 0.60:
        return 3  # Sleep

    # Use coffee carefully to boost alertness within safe limits
    if 0.60 <= alertness < 0.70 and hypertension <= 0.20 and intoxication <= 0.10:
        return 1  # Drink coffee and work

    # Avoid beer unless alertness is critically low and it's safe intoxication-wise
    if alertness < 0.65 and intoxication <= 0.10:
        return 2  # Drink beer and work

    # Default to just working when conditions are stable
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)