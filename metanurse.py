import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if any critical health indicator is met
    if alertness < 0.4 or hypertension > 0.045 or intoxication > 0.03 or time_since_slept >= 4.0:
        return 3

    # Use coffee to boost moderate alertness if health metrics allow
    if 0.4 <= alertness < 0.6 and hypertension < 0.04 and intoxication < 0.025:
        return 1

    # Safe to work if alertness is reasonably high and health indicators are stable
    if alertness >= 0.6 and hypertension < 0.03 and intoxication < 0.02:
        return 0

    # Avoid beer unless alertness is very low, keeping intoxication minimal
    if work_done < 0.01 and intoxication <= 0.01 and alertness < 0.25:
        return 2

    # Default to working if conditions slightly mismatch
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)