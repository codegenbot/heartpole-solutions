import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Always prioritize sleeping to recover alertness early and maintain health
    if alertness < 0.3 or time_since_slept > 10:
        return 3  # Sleep immediately for critical recovery
    
    # Use coffee sparingly but effectively before alertness dips
    if alertness < 0.5 and hypertension <= 0.25 and intoxication <= 0.15:
        return 1  # Coffee to boost alertness without a high hypertensive risk
    
    # Avoid beer unless all conditions are in favorable ranges
    if alertness < 0.4 and intoxication < 0.15:
        return 2  # Beer only when intoxication and alertness are both low-risk
    
    # Optimal condition to work without stimulation
    if alertness >= 0.7 and hypertension <= 0.2 and intoxication <= 0.1:
        return 0  # Best choice when conditions are favorable
    
    # Default to working if moderately capable and not in need of immediate recovery
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)