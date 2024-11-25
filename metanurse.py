import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep for better wellness
    if alertness < 0.5 or time_since_slept > 5 or hypertension > 0.5:
        return 3  # Sleep

    # Just work if conditions are optimal
    if alertness > 0.85 and hypertension < 0.3 and intoxication < 0.01:
        return 0  # Just work

    # More cautious coffee use with tighter health checks
    if 0.7 <= alertness <= 0.85 and hypertension < 0.35 and intoxication < 0.03:
        return 1  # Drink coffee and work

    # Use beer very cautiously with near-zero intoxication/hypertension
    if 0.5 <= alertness < 0.7 and intoxication < 0.01 and hypertension < 0.2:
        return 2  # Drink beer and work

    # Default to sleeping for better recovery if demands aren't met
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)