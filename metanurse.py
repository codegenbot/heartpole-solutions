import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if any bad health indicator
    if alertness < 0.5 or hypertension > 0.04 or intoxication > 0.02 or time_since_slept >= 3.5:
        return 3

    # Use coffee only if alertness is moderate and health metrics allow
    if 0.5 <= alertness < 0.65 and hypertension < 0.03 and intoxication < 0.02:
        return 1

    # Safe to work if alertness is high and health indicators are stable
    if alertness >= 0.65 and hypertension < 0.025 and intoxication < 0.015:
        return 0

    # Avoid beer unless in very specific scenarios which are likely unhealthy
    if work_done < 0.01 and intoxication <= 0.015 and alertness < 0.28:
        return 2

    # Default to working if conditions slightly mismatch
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)