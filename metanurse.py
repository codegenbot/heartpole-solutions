import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if health parameters are at risk
    if alertness < 0.4 or hypertension > 0.6 or intoxication > 0.4 or time_since_slept > 5:
        return 3  # Prioritize sleep

    # Use coffee to boost alertness only when safe
    if 0.4 <= alertness < 0.7 and hypertension <= 0.4 and intoxication <= 0.2:
        return 1  # Drink coffee and work

    # Work directly if alertness is stable and health is good
    if alertness >= 0.7 and hypertension <= 0.4 and intoxication <= 0.2:
        return 0  # Just work

    # Consider beer if intoxication and stress can be managed
    if 0.2 < intoxication < 0.4 and hypertension < 0.4:
        return 2  # Drink beer and work

    return 3  # Default to safe action: sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)