import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if time_since_slept > 7 or alertness < 0.4 or hypertension > 0.75:
        return 3                      # Sleep if conditions are too risky
    if alertness > 0.7 and hypertension < 0.3 and intoxication < 0.1:
        return 0                      # Work if alert and healthy
    if 0.6 <= alertness <= 0.7 and hypertension < 0.5:
        return 1                      # Coffee and work if moderately alert
    if 0.5 <= alertness < 0.6 and intoxication < 0.15 and hypertension < 0.25:
        return 2                      # Beer and work if alertness is low yet manageable
    return 3                          # Default to sleep as a safe fallback

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)