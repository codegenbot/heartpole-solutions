import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.3 or hypertension > 0.75 or intoxication > 0.5 or time_since_slept > 9:
        return 3  # Prioritize sleep

    if alertness > 0.85 and hypertension < 0.5 and intoxication < 0.2:
        return 0  # Work if conditions are optimal

    if 0.6 <= alertness <= 0.85 and hypertension < 0.6 and intoxication < 0.2:
        return 1  # Use coffee to boost productivity safely

    if 0.4 <= alertness < 0.6 and intoxication < 0.15 and hypertension < 0.4:
        return 2  # Use beer sparingly for alertness

    if time_since_slept >= 8 or alertness < 0.6:
        return 3  # Sleep if moderately deprived or low alertness

    return 3  # Fallback to sleep if conditions are not met

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)