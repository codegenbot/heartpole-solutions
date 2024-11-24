import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if time_since_slept > 7 or hypertension > 0.65 or intoxication > 0.55 or alertness < 0.4:
        return 3  # Must sleep due to poor health indicators
    
    if alertness > 0.8 and hypertension < 0.25 and intoxication < 0.2:
        return 0  # Just work, optimal conditions

    if 0.55 <= alertness < 0.8 and hypertension < 0.3 and intoxication < 0.25:
        return 1  # Drink coffee, slight boost needed but no health risk

    if alertness < 0.55 and intoxication < 0.2:
        return 2  # Drink beer, when alertness is low but without immediate health issues

    return 3  # Default to sleep if no conditions match a productive state

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)