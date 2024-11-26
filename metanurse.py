import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Critical health management: Sleep in case of high risk
    if hypertension > 0.03 or intoxication > 0.04:
        return 3
    if time_since_slept > 6:
        return 3

    # Caffeine boost when alertness is low and health risks are low
    if alertness < 0.7 and hypertension < 0.02 and intoxication < 0.02:
        return 1

    # Continue working efficiently if in optimal condition
    if alertness >= 0.7 and hypertension < 0.015 and intoxication < 0.015:
        return 0

    # Ensure periodic rest to prevent exhaustion
    if work_done > 15 and time_elapsed > 30:
        return 3

    # Default fallback: Sleep to recover
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)