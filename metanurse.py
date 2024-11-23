import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if necessary
    if (
        alertness < 0.5
        or hypertension > 0.5
        or intoxication > 0.3
        or time_since_slept >= 7
    ):
        return 3  # Critical health levels, prioritize sleep

    # Use coffee to safely boost alertness when needed
    if alertness < 0.7 and hypertension <= 0.4 and intoxication <= 0.1:
        return 1  # Coffee for gaining alertness safely

    # Manage stress with beer but be cautious of hypertension
    if 0.4 < hypertension <= 0.5 and intoxication <= 0.15:
        return 2  # Beer for stress management

    # Default to working if conditions are optimal
    if alertness >= 0.8 and hypertension < 0.3 and intoxication < 0.1:
        return 0  # Safe to work

    # Rely on default working action if no critical issues detected
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)