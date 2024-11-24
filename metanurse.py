import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if alertness is critically low or no sleep for a long period
    if alertness < 0.5 or time_since_slept > 6:
        return 3  # Sleep

    # Drink coffee and work, if alertness is moderate and hypertension/intoxication are low
    if alertness < 0.6 and hypertension < 0.4 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Work if ideal conditions
    if alertness >= 0.7 and hypertension <= 0.3 and intoxication <= 0.1:
        return 0  # Just work

    # Sleep if hypertension or intoxication is high to avoid health risk
    if hypertension > 0.5 or intoxication > 0.4:
        return 3  # Sleep

    # Drink beer and work to manage stress without exceeding intoxication limits
    if intoxication <= 0.3 and hypertension < 0.5:
        return 2  # Drink beer and work

    return 0  # Default to just work if above conditions are not met

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)