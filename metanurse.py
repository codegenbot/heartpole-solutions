import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for critical health issues
    if hypertension > 0.012 or intoxication > 0.05:
        return 3

    # Sleep if alertness is very low or sleep deprivation is considerable
    if alertness < 0.7 or time_since_slept > 2.5:
        return 3
    
    # Drink coffee for moderate increase in alertness while staying safe
    if alertness < 0.85 and hypertension < 0.01 and intoxication < 0.02:
        return 1

    # If slightly intoxicated but alert, beer can slightly adjust it with risk
    if intoxication > 0.02 and intoxication < 0.05 and alertness > 0.8:
        return 2

    # Default to just work if conditions are good
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)