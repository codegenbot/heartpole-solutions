import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize health by managing hypertension and intoxication
    if hypertension > 0.5 or intoxication > 0.3:
        return 3  # Sleep

    # Sleep if alertness is very low or time since last rest is too long
    if alertness < 0.5 or time_since_slept > 10:
        return 3  # Sleep

    # Drink coffee and work if alertness is low and less work is done
    if alertness < 0.7 and work_done < 0.5:
        return 1  # Drink coffee and work

    # Opt for work when conditions are relatively good
    if alertness >= 0.7 and hypertension < 0.3 and intoxication < 0.2:
        return 0  # Just work

    # Default to sleep for recovery
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)