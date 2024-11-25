import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.6 or intoxication > 0.3 or alertness < 0.4 or time_since_slept > 10:
        return 3  # Prioritize sleep if health indicators are critical
    if alertness < 0.6 and hypertension < 0.4 and intoxication < 0.25:
        return 1  # Use coffee to boost alertness but consider hypertension
    if 0.1 < intoxication < 0.3 and hypertension < 0.5 and alertness > 0.5:
        return 2  # Use beer to moderate intoxication if conditions allow
    return 0  # Default to work if stable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)