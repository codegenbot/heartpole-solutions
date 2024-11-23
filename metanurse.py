def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep in more conservative conditions
    if (
        alertness < 0.7
        or hypertension > 0.4
        or intoxication > 0.2
        or time_since_slept >= 5
    ):
        return 3  # Sleep is prioritized more cautiously

    # Use coffee only if sufficiently alert and stress is manageable
    if alertness < 0.8 and hypertension <= 0.35 and intoxication <= 0.1:
        return 1  # Coffee for boosting alertness safely

    # Allow beer only when slightly elevated hypertension but low intoxication
    if 0.3 < hypertension <= 0.4 and intoxication <= 0.2:
        return 2  # Beer for stress management, with caution

    # Optimal conditions to just work
    if alertness >= 0.8 and hypertension < 0.3 and intoxication < 0.1:
        return 0  # Safe to focus on work

    return 0  # Default safe action


import sys

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)