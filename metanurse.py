import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Rest when health indicators suggest serious degradation
    if alertness < 0.5 or hypertension > 0.07 or intoxication > 0.04 or time_since_slept >= 2.5:
        return 3  # Sleep if any health indicators are concerning.

    # Use coffee to boost productivity when alertness is medium and health is stable
    if 0.55 <= alertness < 0.75 and hypertension < 0.05 and intoxication < 0.03:
        return 1  # Coffee is optimal for medium alertness with manageable stress levels.

    # Ensure working with high alertness
    if alertness >= 0.75 and hypertension < 0.04 and intoxication < 0.02:
        return 0  # Work if indicators suggest strong health and alertness.

    # Avoid beer (intoxication risk), prefer default or rest if unsure
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)