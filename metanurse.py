import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleeping to maintain health
    if time_since_slept > 8 or alertness < 0.5:
        return 3  # Sleep
    # Use coffee effectively
    if alertness >= 0.6 and hypertension < 0.3 and intoxication < 0.2:
        return 1  # Drink coffee and work
    # Use beer only when safe
    if 0.3 <= intoxication < 0.5 and hypertension <= 0.4:
        return 2  # Drink beer and work
    # Choose work when health supports it
    if alertness >= 0.8 and hypertension < 0.35 and intoxication < 0.1:
        return 0  # Just work
    # Fallback to sleep if others are not suitable
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)