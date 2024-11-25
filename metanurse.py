import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if alertness is low or too long without sleep
    if alertness < 0.6 or time_since_slept > 8 or hypertension > 0.6:
        return 3  # Sleep

    # Work with coffee for moderate alertness when health indicators are acceptable
    if 0.6 <= alertness < 0.75 and hypertension <= 0.5 and intoxication <= 0.15:
        return 1  # Drink coffee and work

    # Work without additional substances if health indicators are optimal
    if alertness >= 0.75 and hypertension <= 0.4 and intoxication <= 0.1:
        return 0  # Just work safely

    # If intoxication is rising, prioritize next steps for health recovery
    if intoxication > 0.2:
        return 3  # Sleep

    # Default to sleeping if conditions are unclear to avoid health issues
    return 3  # Default to sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)