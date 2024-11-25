import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Adjusted thresholds to better balance productivity and health
    if hypertension > 0.7 or intoxication > 0.3 or alertness < 0.4 or time_since_slept > 10:
        return 3  # Increased threshold for sleep to prevent serious health issues
    if alertness < 0.6 and hypertension < 0.4 and intoxication < 0.2:
        return 1  # Conditions to safely enhance alertness with coffee
    if 0.1 < intoxication < 0.2 and hypertension < 0.5 and alertness > 0.5:
        return 2  # Allow beer cautiously under certain balanced conditions
    return 0  # Focus on work otherwise

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)