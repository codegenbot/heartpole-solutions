import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Priortize sleep for high health risks
    if hypertension > 0.3 or intoxication > 0.2:
        return 3
    # Prioritize sleep if low alertness or long time without sleep
    if alertness < 0.5 or time_since_slept > 4:
        return 3
    # Drink coffee to boost alertness when moderately low
    if alertness < 0.7 and hypertension < 0.2 and intoxication < 0.1:
        return 1
    # Drink beer when very alert for minor boost
    if alertness >= 0.85 and hypertension <= 0.1 and intoxication < 0.02 and work_done < 0.3:
        return 2
    # Default to work in all other conditions
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)