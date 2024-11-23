import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep conditions
    if (
        hypertension > 0.5 or intoxication > 0.3 or alertness < 0.4 or 
        time_since_slept >= 12
    ):
        return 3  # Sleep if there's a notable health risk or alertness drop
    
    # Beer for stress relief if condition allows
    if intoxication < 0.25 and hypertension > 0.45:
        return 2  # Drink beer if moderate hypertension with manageable intoxication
    
    # Coffee conditions
    if alertness < 0.6 and hypertension <= 0.35 and intoxication <= 0.2:
        return 1  # Drink coffee to maintain productivity safely

    # Optimal work conditions
    if alertness >= 0.7 and hypertension < 0.25 and intoxication <= 0.15:
        return 0  # Just work if health and alertness are excellent

    # Default: if in acceptable health state, work
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)