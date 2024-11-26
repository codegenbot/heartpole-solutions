import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep if serious health risks are present
    if hypertension > 0.06 or intoxication > 0.05:
        return 3

    # Prioritize sleep if very low alertness or > 4.5 hours without sleep
    if time_since_slept >= 4.5 or alertness < 0.3:
        return 3

    # Use coffee more liberally if health indicators are stable
    if 0.3 <= alertness < 0.6 and hypertension < 0.03 and intoxication < 0.02:
        return 1

    # Proceed with work if alertness is adequate and health is very good
    if alertness >= 0.7 and hypertension < 0.015 and intoxication < 0.01:
        return 0

    # Default to coffee and work as productivity priority when health is stable
    return 1

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)