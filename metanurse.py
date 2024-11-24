import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep in more cautious scenarios
    if alertness < 0.5 or hypertension > 0.6 or intoxication >= 0.3 or time_since_slept > 7:
        return 3  # Must sleep

    # Prioritize direct work with good conditions
    if alertness >= 0.7 and hypertension <= 0.3 and intoxication < 0.1:
        return 0  # Just work

    # Use coffee judiciously to boost focus within stricter alertness ranges
    if alertness < 0.7 and hypertension < 0.5 and intoxication <= 0.2:
        return 1  # Drink coffee and work

    # Beer as a last resort with stricter conditions
    if 0.6 <= alertness < 0.7 and hypertension < 0.4 and intoxication < 0.2:
        return 2  # Drink beer and work

    return 3  # Default to sleep if uncertain

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)