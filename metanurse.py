import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Always prioritize sleep when the body shows any serious risk
    if (
        alertness < 0.3
        or hypertension > 0.8
        or intoxication > 0.5
        or time_since_slept > 7
    ):
        return 3

    # Use coffee when moderately tired and safe from health issues
    if (
        alertness < 0.5
        and hypertension <= 0.6
        and intoxication < 0.3
        and time_since_slept <= 5
    ):
        return 1

    # Work if alertness is satisfactory and health indicators are safe
    if alertness >= 0.6 and hypertension < 0.5 and intoxication < 0.25:
        return 0

    # Default to sleep for anything else to ensure rejuvenation
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)