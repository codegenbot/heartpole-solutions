import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if necessary by using stricter thresholds
    if time_since_slept > 14 or alertness < 0.4:
        return 3  # Sleep
    
    # Prioritize health by considering safe thresholds
    if hypertension > 0.2 or intoxication > 0.1:
        return 3  # Sleep

    # Use coffee to boost when slightly fatigued
    if alertness < 0.7 and hypertension <= 0.15 and intoxication <= 0.05:
        return 1  # Drink coffee and work

    # Use beer to maintain morale if conditions allow
    if alertness >= 0.9 and hypertension <= 0.1 and intoxication <= 0.05:
        return 2  # Drink beer and work

    # Default to working in optimal conditions
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)