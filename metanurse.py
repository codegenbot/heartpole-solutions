import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if any indicator shows unhealthy levels
    if alertness < 0.5 or time_since_slept > 8 or hypertension > 0.5 or intoxication > 0.1:
        return 3  # Sleep

    # Work when conditions are optimal and health metrics are good
    if alertness > 0.7 and hypertension < 0.3 and intoxication < 0.05:
        return 0  # Just work

    # Use coffee wisely to improve alertness without worsening health conditions
    if 0.5 <= alertness <= 0.7 and hypertension < 0.4 and intoxication < 0.1:
        return 1  # Drink coffee and work

    # Default to sleeping if optimum conditions for working are not met
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)