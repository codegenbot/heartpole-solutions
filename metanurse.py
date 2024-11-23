import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.6 or intoxication > 0.35:
        return 3  # Sleep to recover from potential health risks
    if time_since_slept > 14:
        return 3  # Sleep if very long time without rest
    if alertness < 0.4:
        return 3  # Sleep if very low alertness
    if alertness < 0.5 and time_since_slept <= 8:
        return 1  # Drink coffee to boost alertness for increased productivity
    if intoxication > 0.25:
        return 2  # Drink beer cautiously if intending to reduce intoxication over time
    if work_done < 0.9:
        return 0  # Continue working if health is under control
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)