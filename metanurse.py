import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Re-prioritize sleeping conditions
    if hypertension > 0.012 or intoxication > 0.035:
        return 3
    
    # Lower threshold for sleep action based on alertness and sleep time
    if alertness < 0.65 or time_since_slept > 2.4:
        return 3

    # More cautious approach to drinking coffee
    if alertness < 0.75 and hypertension < 0.009 and intoxication < 0.018:
        return 1

    # Restrict beer to specific narrow conditions
    if 0.65 <= alertness < 0.75 and 0.01 < hypertension <= 0.012 and intoxication < 0.025:
        return 2

    # Default to working in stable conditions
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)