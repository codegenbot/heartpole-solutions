import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if health issues are significant or if alertness is very low
    if alertness < 0.6 or hypertension > 0.5 or intoxication > 0.4 or time_since_slept > 6:
        return 3  # Sleep

    # Use coffee for a productivity boost when alertness is moderate and health is reasonable
    if 0.6 <= alertness < 0.8 and hypertension < 0.5 and intoxication <= 0.3:
        return 1  # Drink coffee and work

    # Work if alertness and health risks are optimal
    if alertness >= 0.8 and hypertension <= 0.3 and intoxication < 0.2 and time_since_slept <= 6:
        return 0  # Just work

    # Enable beer usage sparingly, mainly if it slightly improves productivity safely
    if 0.7 <= alertness < 0.8 and intoxication < 0.25 and hypertension < 0.35:
        return 2  # Drink beer and work

    return 3  # Default to sleep if other conditions are not met

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)