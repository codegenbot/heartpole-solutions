import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Check for any critical condition first
    if intoxication > 0.2 or hypertension > 0.02:
        return 3
    if time_since_slept >= 7:
        return 3
    # If moderately intoxicated or slightly hypertensive, choose less risky actions
    if hypertension > 0.015 or intoxication > 0.1:
        return 2  # drink beer and work
    # Optimizing productivity based on alertness
    if alertness < 0.5:
        return 3  # sleep if alertness is low
    if 0.5 <= alertness < 0.6:
        return 1  # drink coffee and work
    return 0  # just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)