import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.03 or intoxication > 0.04:
        return 3  # Prioritize sleep if health is compromised

    if time_since_slept > 3.5:
        return 3  # Sleep if it's been a while, even if indicators aren't high

    if alertness < 0.7 and hypertension <= 0.015:
        return 1  # Drink coffee if alertness is low and it's safe

    if alertness >= 0.8 and intoxication <= 0.02:
        return 0  # Work normally if alertness is good and sober

    if alertness >= 0.6 and intoxication > 0.02 and intoxication <= 0.05:
        return 2  # Use beer if mildly intoxicated and alert

    return 0  # Default to working if nothing else

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)