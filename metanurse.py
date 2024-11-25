import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Priority given to recovery if thresholds exceeded
    if alertness < 0.4 or time_since_slept > 8 or hypertension > 0.75 or intoxication > 0.4:
        return 3  # Sleep

    # High-priority work condition
    if alertness >= 0.8 and hypertension < 0.6 and intoxication < 0.15:
        return 0  # Just work
    
    # Moderate use of coffee for sustaining alertness
    if 0.6 <= alertness < 0.8 and hypertension < 0.65:
        return 1  # Coffee and work

    # Use beer sparingly for relaxation without highly impacting productivity
    if alertness < 0.6 and hypertension < 0.5 and intoxication < 0.25:
        return 2  # Beer and work
    
    # Default to sleeping if conditions are not ideal
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)