import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep only when serious health risks are detected
    if hypertension > 0.75 or intoxication > 0.7:
        return 3  # Sleep

    # Sleep if alertness or sleep time is critically low
    if alertness < 0.4 or time_since_slept > 7:
        return 3  # Sleep

    # Best conditions for just working
    if alertness > 0.7 and hypertension < 0.4 and intoxication < 0.3:
        return 0  # Just work

    # Drink coffee to boost productivity if alertness and hypertension are moderate
    if 0.5 <= alertness < 0.7 and hypertension < 0.5:
        return 1  # Drink coffee and work

    # If work_done is too low and hypertension, intoxication are within control, push for work
    if work_done < (0.6 * time_elapsed) and hypertension < 0.5 and intoxication < 0.5:
        return 0  # Just work

    # Default is to rest to recover if nothing is optimal or critical
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)