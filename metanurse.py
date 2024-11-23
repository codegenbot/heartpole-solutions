import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Adjusted sleep conditions to prioritize health more
    if alertness < 0.6 or hypertension > 0.5 or intoxication > 0.3 or time_since_slept >= 6:
        return 3  # Sleep prioritization

    # Check for productivity boost within safety limits
    if alertness < 0.7 and hypertension < 0.4:
        return 1  # Coffee to safely boost productivity

    # Allow beer only if moderately stressed and low intoxication
    if 0.4 < hypertension <= 0.5 and intoxication < 0.2:
        return 2  # Beer under safer conditions

    # Direct work if conditions are optimal
    if alertness >= 0.7 and hypertension < 0.3 and intoxication < 0.1:
        return 0  # Work is safe

    return 0  # Default to work if all else is bypassed

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)