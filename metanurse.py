import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if significant health risks are present
    if alertness < 0.4 or hypertension > 0.7 or intoxication > 0.2 or time_since_slept >= 5:
        return 3  # Sleep

    # Drink coffee if alertness is below optimal and low health risks
    if alertness < 0.6 and hypertension <= 0.5 and intoxication <= 0.1:
        return 1  # Coffee and work

    # Opt to work if alertness and health indicators are positive
    if alertness >= 0.65 and hypertension <= 0.5:
        return 0  # Just work

    # Avoid beer as it can increase intoxication
    return 0  # Default to just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)