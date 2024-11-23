import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate rest for serious health conditions
    if hypertension > 0.4 or intoxication > 0.4:
        return 3  # Sleep

    # Rest if accumulated tiredness is significant or alertness is critically low
    if alertness < 0.4 or time_since_slept > 15:
        return 3  # Sleep

    # Moderate use of coffee if early in the day or mild fatigue
    if alertness < 0.75 and time_elapsed < 5:
        return 1  # Drink coffee and work

    # Allow beer break for slight relaxation if close to a full work day
    if work_done > 0.8 and intoxication < 0.2 and time_elapsed > 8:
        return 2  # Drink beer and work

    # Default to work if health metrics are typically stable
    if alertness > 0.6 and hypertension < 0.25 and intoxication < 0.2:
        return 0  # Just work
    
    # Prefer rest to recalibrate if no suitable work condition
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)