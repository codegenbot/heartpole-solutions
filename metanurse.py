import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.75 or intoxication > 0.55 or time_since_slept > 7:
        return 3  # Prioritize sleep for recovery if any health risk parameters are high
    if alertness < 0.4:
        return 1  # Use coffee more aggressively when alertness is low
    if alertness < 0.7 and hypertension <= 0.6 and intoxication <= 0.2:
        return 1  # Drink coffee if alertness is below optimal and health is stable
    if hypertension > 0.6 and intoxication > 0.25:
        return 3  # Sleep when both hypertension and intoxication are increasing
    if alertness >= 0.8 and hypertension < 0.5 and intoxication < 0.1:
        return 0  # Optimal state for productivity
    if hypertension <= 0.55 and intoxication <= 0.3:
        return 2  # Drink beer when minor stress but not more than moderate levels
    return 3  # Conservative default to ensure staying healthy

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)