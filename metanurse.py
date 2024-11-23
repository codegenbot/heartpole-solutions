import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate rest for serious health conditions
    if hypertension > 0.3 or intoxication > 0.3:
        return 3  # Sleep

    # Rest if alertness is low or if too much time has passed since last sleep
    if alertness < 0.5 or time_since_slept > 10:
        return 3  # Sleep

    # Cautious use of coffee if it's still early in the session
    if alertness < 0.7 and time_elapsed < 6:
        return 1  # Drink coffee and work

    # Allow beer for a slight morale boost only if nearing project completion
    if work_done > 0.85 and intoxication < 0.1 and time_elapsed > 7:
        return 2  # Drink beer and work

    # Default to just work if overall conditions are reasonable
    if alertness > 0.7 and hypertension < 0.2 and intoxication < 0.1:
        return 0  # Just work
    
    # Default to sleep if no better option
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)