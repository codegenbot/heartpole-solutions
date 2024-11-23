import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health
    if hypertension > 0.25 or intoxication > 0.2:
        return 3  # Sleep
    
    # Encourage rest and balance productivity with health
    if time_since_slept > 6 or alertness < 0.6:
        return 3  # Sleep

    # Use coffee moderately
    if 0.6 <= alertness < 0.8 and hypertension <= 0.15 and intoxication <= 0.1:
        return 1  # Drink coffee and work

    # Default to working more reliably while balancing health
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)