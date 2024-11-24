import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep when alertness is very low or sleeplessness is prolonged
    if time_since_slept > 8 or alertness < 0.3:
        return 3

    # Avoid excessive hypertension or intoxication
    if hypertension > 0.7 or intoxication > 0.6:
        return 3

    # If alertness can be safely boosted, drink coffee
    if 0.3 <= alertness < 0.5 and hypertension <= 0.6 and intoxication < 0.3:
        return 1

    # Opt to work with beer if alertness is moderate but needs a boost and safe to do so
    if intoxication < 0.2 and alertness < 0.5 and hypertension < 0.5:
        return 2

    # If conditions are optimal, just work
    if alertness >= 0.5 and hypertension < 0.5 and intoxication < 0.1:
        return 0

    # Default to minimal action to avoid health risks
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)