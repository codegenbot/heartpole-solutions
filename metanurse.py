import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Priority given to recovery if thresholds exceeded
    if alertness < 0.3 or hypertension > 0.8 or intoxication > 0.5 or time_since_slept > 10:
        return 3  # Sleep

    # High-priority work condition
    if alertness > 0.75 and hypertension < 0.7 and intoxication < 0.2:
        return 0  # Just work

    # Moderate use of coffee for sustaining alertness
    if 0.5 <= alertness < 0.75 and hypertension < 0.65 and intoxication < 0.1:
        return 1  # Coffee and work

    # Use beer sparingly for relaxation without highly impacting productivity
    if alertness < 0.5 and hypertension < 0.55 and intoxication < 0.3:
        return 2  # Beer and work
    
    # Default to sleeping if conditions are not ideal
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)