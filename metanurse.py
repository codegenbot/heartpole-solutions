import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep priority for critical health risks
    if alertness < 0.2 or hypertension > 0.6 or intoxication > 0.3 or time_since_slept > 10:
        return 3  # Critical health issues demand sleep

    # Use coffee judiciously, ensuring hypertension and intoxication are controlled
    if 0.2 <= alertness < 0.6 and hypertension <= 0.5 and intoxication <= 0.2:
        return 1  # Coffee if alertness boost is needed without health risks

    # Work condition must be more conservative on alertness
    if alertness >= 0.6 and hypertension <= 0.4 and intoxication <= 0.15:
        return 0  # Conditions optimal for work

    # Use beer extremely cautiously when both health indicators are low
    if intoxication < 0.1 and hypertension < 0.3:
        return 2  # Only use beer if it can boost and risks are minimal

    # Default to sleep if in doubt
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)