import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.8 or intoxication > 0.5 or time_since_slept > 10:
        return 3  # Sleep if health is at significant risk
    if time_since_slept > 8 or alertness < 0.4:
        return 3  # Ensure adequate sleep
    if alertness < 0.6 and hypertension < 0.7 and intoxication < 0.3:
        return 1  # Coffee to improve alertness but only if health permits
    if alertness >= 0.6 and hypertension < 0.5 and intoxication < 0.2:
        return 0  # Just work, as health metrics are in good standing
    return 2  # Use beer sparingly if slight intoxication is acceptable for next actions

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)