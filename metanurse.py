import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.7 or intoxication > 0.6:
        return 3  # Prioritize sleep if health parameters are high-risk
    if time_since_slept > 8:
        return 3  # Sleep if sleep deprivation is significant
    if alertness < 0.4:
        return 3  # Sleep if alertness is too low
    if 0.4 <= alertness < 0.6:
        if hypertension < 0.5 and intoxication < 0.3:
            return 1  # Drink coffee carefully to boost alertness
    return 0  # Work when adequately alert

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)