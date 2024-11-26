import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if very low alertness or > 4.0 hours without sleep
    if time_since_slept >= 4.0 or alertness < 0.3:
        return 3

    # Immediate sleep if serious health risks are present
    if hypertension > 0.07 or intoxication > 0.06:
        return 3

    # Use coffee for moderate alertness if health is stable
    if 0.4 <= alertness < 0.6 and hypertension < 0.04 and intoxication < 0.03:
        return 1

    # Proceed with work if health is very good and alertness is high
    if alertness >= 0.8 and hypertension < 0.02 and intoxication < 0.01:
        return 0

    # Sleep if unsure between snack options for long-term stability
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)