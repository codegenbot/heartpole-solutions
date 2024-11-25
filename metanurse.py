import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep when severely tired or intoxicated
    if time_since_slept > 8 or alertness < 0.4 or intoxication > 0.1:
        return 3

    # Use coffee if moderately tired but within safe health limits
    if alertness < 0.6 and hypertension < 0.05 and intoxication < 0.05:
        return 1

    # Work is optimal if alert and healthy
    if alertness >= 0.7 and hypertension < 0.05 and intoxication < 0.03:
        return 0

    # Beer as last resort if nothing else improves health/productivity trade-off
    if work_done < 0.02 and intoxication <= 0.02 and alertness < 0.3:
        return 2

    # Default action conservatively
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)