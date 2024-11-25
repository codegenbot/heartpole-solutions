import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.2 or intoxication > 0.1 or time_since_slept > 10:
        return 3  # Sleep if health risks are present
    if time_since_slept > 6 or alertness < 0.3:
        return 3  # Sleep if sufficiently tired or alertness is low
    
    if alertness < 0.5 and hypertension <= 0.15:
        return 1  # Drink coffee only if blood pressure is within safe range
    
    if alertness >= 0.7 and hypertension < 0.1 and intoxication < 0.05:
        return 0  # Optimal conditions to just work
    return 0  # Default to just working

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)