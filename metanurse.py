import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping if significant health issues or exceeding time awake
    if hypertension > 0.5 or intoxication > 0.35 or time_since_slept >= 10:
        return 3
    
    # Use coffee judiciously to boost moderate alertness only if hypertension is low
    if 0.3 <= alertness < 0.6 and hypertension < 0.4:
        return 1

    # Proceed to work normally if alertness is high with low health risks
    if alertness >= 0.6 and hypertension < 0.2 and intoxication < 0.15:
        return 0

    # Choose beer to manage mild intoxication situation
    if intoxication < 0.25:
        return 2

    # Default to work if above criteria do not match
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)