import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep priority for critical health risks
    if alertness < 0.3 or hypertension > 0.5 or intoxication > 0.2 or time_since_slept > 8:
        return 3  # Critical health issues demand sleep

    # Use coffee if moderate alertness needed and health allows
    if 0.3 <= alertness < 0.5 and hypertension <= 0.4 and intoxication <= 0.15:
        return 1  # Coffee if it can boost safely

    # Work if alertness is good and health is stable
    if alertness >= 0.5 and hypertension <= 0.3 and intoxication <= 0.1:
        return 0  # Good conditions for work

    # Extremely cautious use of beer for a minor boost if all health indicators are low risk
    if intoxication < 0.05 and hypertension < 0.2:
        return 2  # Beer if low risks

    # Default to sleep when uncertain or slightly risky
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)