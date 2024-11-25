import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if time_since_slept > 6 or alertness < 0.5 or hypertension > 0.7:
        return 3                      # Sleep is prioritized based on updated conditions
    if alertness >= 0.75 and hypertension < 0.25 and intoxication < 0.05:
        return 0                      # Work when all parameters are optimal
    if 0.6 <= alertness < 0.75 and hypertension < 0.4:
        return 1                      # Coffee and work if moderately alert and safe
    if 0.5 <= alertness < 0.6 and intoxication < 0.1 and hypertension < 0.2:
        return 2                      # Beer and work based on manageable conditions
    return 3                          # Default to sleep as a safer fallback

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)