import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.6 or intoxication > 0.5:
        return 3  # Sleep to mitigate health risks
    if time_since_slept > 10 or alertness < 0.3:
        return 3  # Sleep due to excessive wakefulness or too low alertness
    if alertness < 0.5:
        return 1  # Drink coffee to improve alertness, if not overly hypertensive
    if alertness >= 0.7 and work_done < 0.9 and hypertension < 0.5:
        return 0  # Just work if good alertness and health is stable
    if intoxication < 0.3 and time_elapsed > 5:
        return 2  # Occasionally drink beer if it's safe, for potential social productivity boost
    return 0  # Default to work if conditions are mildly favorable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)