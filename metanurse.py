import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate action if health is seriously at risk
    if hypertension >= 0.015 or intoxication >= 0.04:
        return 3  # Sleep to ensure health and mitigate immediate risks

    # Prioritize sleep if sleep-deprived or very low alertness
    if time_since_slept >= 4 or alertness < 0.4:
        return 3  # Engage sleep recovery

    # Use coffee strategically when moderate improvements can be made
    if alertness < 0.7 and hypertension < 0.01 and intoxication < 0.02:
        return 1  # Coffee to enhance alertness safely

    # Work as default if all health indicators are within optimal limits
    return 0  # Maintain focus on productivity when conditions allow

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)