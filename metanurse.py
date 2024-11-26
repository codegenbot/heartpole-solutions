import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if alertness is low or haven't slept recently
    if alertness < 0.6 or time_since_slept >= 6.0:
        return 3

    # Avoid severe health risks by checking hypertension and intoxication
    if hypertension > 0.04 or intoxication > 0.02:
        return 3

    # Use coffee to boost moderate alertness if low health risks
    if 0.6 <= alertness < 0.8 and hypertension <= 0.02 and intoxication <= 0.01:
        return 1

    # Default to just working if alertness is adequate and health risks are managed
    if 0.8 <= alertness < 0.9 or (0.9 <= alertness and hypertension <= 0.01 and intoxication <= 0.01):
        return 0

    # Tightly restrict beer usage - not advised
    if alertness > 0.9 and intoxication <= 0.01:
        return 2

    # Default to working if no other conditions are met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)