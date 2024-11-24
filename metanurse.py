import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if signs of significant health risks
    if alertness < 0.4 or hypertension > 0.6 or intoxication > 0.25 or time_since_slept >= 6:
        return 3  # Sleep

    # Drink coffee if alertness is low and other conditions permit
    if alertness < 0.6 and hypertension <= 0.4 and intoxication <= 0.1:
        return 1  # Coffee and work

    # Work if alertness is good and health indicators are under control
    if alertness >= 0.65 and hypertension <= 0.5 and intoxication <= 0.15:
        return 0  # Just work

    # Default to beer if conditions are tolerable and no sleeping needed
    if intoxication < 0.2:
        return 2  # Beer and work

    # Default action in uncertain scenarios
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)