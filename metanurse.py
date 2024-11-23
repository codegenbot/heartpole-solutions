import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate health-first actions
    if hypertension > 0.5 or intoxication > 0.4:
        return 3  # Immediate sleep for high hypertension or intoxication
    
    # Consider sleep if lack of rest or low alertness
    if time_since_slept > 10 or alertness < 0.3:
        return 3  # Sleep needed due to long waking time or very low alertness

    # Caffeine should be safe and beneficial for low alertness
    if alertness < 0.4 and hypertension < 0.25:
        return 1  # Use coffee to safely boost alertness

    # Avoid beer when intoxication levels are considerable
    if alertness < 0.5 and intoxication < 0.15:
        return 2  # Beer justified with caution on intoxication limits

    # Favor neutral, incremental work when conditions are met
    if alertness >= 0.5 and hypertension <= 0.2 and intoxication <= 0.1:
        return 0  # Work under favorable conditions
    
    # Default to basic work otherwise
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)