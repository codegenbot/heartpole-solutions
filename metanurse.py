import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Always prioritize sleep if alertness or time_since_slept is critical
    if alertness < 0.4 or time_since_slept > 6 or hypertension > 0.6:
        return 3  # Sleep

    # If alertness is optimal and health conditions are ideal
    if alertness > 0.8 and hypertension < 0.3 and intoxication == 0.0:
        return 0  # Just work

    # Use coffee when alertness is moderate, and health permits
    if 0.6 <= alertness <= 0.8 and hypertension < 0.4 and intoxication < 0.05:
        return 1  # Drink coffee and work

    # Avoid beer unless alertness is bordering sleepiness without high intoxication
    if 0.4 <= alertness < 0.6 and intoxication < 0.05 and hypertension < 0.3:
        return 2  # Drink beer and work

    # Default to sleeping if above conditions are not met
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)