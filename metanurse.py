import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Opt for sleep sooner to maintain health
    if hypertension > 0.5 or intoxication > 0.3 or alertness < 0.2 or time_since_slept > 14:
        return 3
    
    # High alertness and low stress conditions - work directly
    if alertness >= 0.75 and hypertension <= 0.2 and intoxication <= 0.05:
        return 0

    # Offer earlier sleep consideration when alertness is low
    if alertness < 0.35 or time_since_slept > 10:
        return 3

    # Use coffee with careful consideration of hypertension
    if 0.35 <= alertness < 0.5 and hypertension <= 0.3:
        return 1
    
    # Even more cautious with beer use, considering very low intoxication
    if 0.25 <= alertness < 0.4 and intoxication < 0.001:
        return 2

    # Default to working if not at an immediate health risk
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)