import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Health precautions
    if alertness < 0.3 or time_since_slept > 8 or intoxication > 0.15:
        return 3  # Urgent need for rest to prevent harm

    # Moderate alertness with low health risks
    if alertness < 0.55 and hypertension < 0.06 and intoxication <= 0.07:
        return 1  # Boost productivity safely with coffee
    
    # Low workload with very low intoxication and slightly low alertness
    if work_done < 0.05 and intoxication <= 0.02 and alertness < 0.45:
        return 2  # Occasionally relax with beer if overall risk is low

    # General productivity mode
    if alertness >= 0.65 and hypertension < 0.03 and intoxication < 0.03:
        return 0  # Safe to work

    # Default conservative approach
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)