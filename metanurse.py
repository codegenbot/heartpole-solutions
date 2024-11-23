import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # More strict sleep criteria
    if alertness < 0.6 or hypertension > 0.5 or intoxication > 0.3 or time_since_slept >= 6:
        return 3  # Prioritize sleep

    # Conservative coffee use
    if alertness < 0.7 and hypertension < 0.45:
        return 1  # Coffee for alertness

    # Allow beer only in mild stress situations
    if 0.35 < hypertension <= 0.45 and intoxication < 0.25:
        return 2  # Beer for moderate stress relief

    # Ideal conditions for just working
    if alertness >= 0.7 and hypertension < 0.35 and intoxication < 0.2:
        return 0  # Safe to work

    return 0  # Default safe action

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)