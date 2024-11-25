import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if alertness or any risky health condition is concerning
    if alertness < 0.5 or hypertension > 0.7 or intoxication > 0.5 or time_since_slept > 16:
        return 3  # Sleep to recover from risky conditions or extreme tiredness

    # If alertness is moderately good, and health indicators don't show risk, work
    if alertness >= 0.7 and hypertension < 0.6 and intoxication < 0.3:
        return 0  # Just work when in fairly good condition

    # Use coffee when alertness needs moderate boosting and risks are manageable
    if 0.5 <= alertness < 0.7 and hypertension < 0.7 and intoxication < 0.3:
        return 1  # Coffee and work to improve alertness safely

    # Avoid beer for better health management; fallback to sleep in ambiguous cases
    return 3  # Default to sleep for conservative health maintenance

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)