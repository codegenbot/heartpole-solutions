import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if time_since_slept > 8 or alertness < 0.4 or hypertension > 0.8 or intoxication > 0.25:
        return 3  # Sleep if health conditions are too risky
    if 0.7 <= alertness <= 0.8 and hypertension < 0.3 and intoxication < 0.15:
        return 1  # Drink coffee and work if alertness is decent but not optimal
    if alertness >= 0.8 and hypertension < 0.3 and intoxication < 0.1:
        return 0  # Just work if conditions are optimal
    if alertness < 0.6 and time_since_slept <= 8:
        return 1  # Boost alertness with coffee if not optimal but manageable
    if intoxication >= 0.15:
        return 2  # Use beer if intoxication is significant to potentially adjust alertness
    return 0  # Continue working by default

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)