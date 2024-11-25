import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if serious health issues detected or awake for too long
    if hypertension > 0.6 or intoxication > 0.4 or time_since_slept >= 6:
        return 3

    # Use coffee to boost alertness only if health permits
    if alertness < 0.5 and hypertension < 0.45 and intoxication < 0.25:
        return 1

    # Opt to work when alertness is sufficient and health is good
    if alertness >= 0.7 and hypertension < 0.3 and intoxication < 0.2:
        return 0

    # Revert to beer if there is only mild health degradation
    return 2

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)