import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if critical levels are reached
    if alertness < 0.5 or hypertension >= 0.7 or intoxication >= 0.5 or time_since_slept > 6:
        return 3  # Must sleep

    # Prioritize steady work if alertness is good and health is stable
    if alertness > 0.9 and hypertension < 0.4 and intoxication < 0.2:
        return 0  # Just work

    # Use coffee if alertness needs boosting and health indicators allow
    if alertness < 0.7 and hypertension < 0.5 and intoxication < 0.25:
        return 1  # Drink coffee and work

    # Use beer cautiously if small relaxation is needed
    if alertness < 0.6 and intoxication < 0.3:
        return 2  # Drink beer and work
        
    return 0  # Default to just work if health is stable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)