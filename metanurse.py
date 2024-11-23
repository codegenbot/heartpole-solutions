import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.7 or intoxication > 0.4:
        return 3  # Sleep to recover from health risks
    if time_since_slept > 16:
        return 3  # Sleep if very long time without rest
    if alertness < 0.4:
        return 3  # Sleep if very low alertness
    if time_since_slept > 12:
        return 3  # Sleep if long time since last sleep
    if alertness < 0.5 and time_since_slept <= 8:
        return 1  # Drink coffee to boost alertness
    if intoxication > 0.2:
        return 2  # Drink beer if intoxication can be reduced during social/work events
    if work_done < 0.9:
        return 0  # Continue working if nothing critical affects health
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)