import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension >= 0.02 or intoxication >= 0.02:  # Be more cautious with health
        return 3  # Sleep if any significant health risks are present
    
    if time_since_slept > 2.5:  # Trigger sleep slightly earlier
        return 3  # Sleep if the user hasn't slept recently enough

    if alertness < 0.6 and hypertension < 0.015:  # Lower threshold for coffee; ensure hypertension is safe
        return 1  # Drink coffee if alertness is significantly declining and hypertension is low

    if alertness > 0.9 and intoxication < 0.005:
        return 0  # Just work if alertness is very high and intoxication is minimal

    if intoxication < 0.01 and time_since_slept < 2.0:
        return 2  # Drink beer and work only if intoxication and time_since_slept are low

    return 0  # Default to working if none of the conditions trigger more urgent actions

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)