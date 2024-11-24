import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep for tiredness or chronic stress
    if alertness < 0.5 or hypertension > 0.7 or intoxication > 0.25 or time_since_slept >= 5:
        return 3  # Sleep

    # Use coffee if alertness and health stats are moderate, with caution
    if 0.5 <= alertness < 0.7 and hypertension <= 0.6 and intoxication <= 0.2:
        return 1  # Coffee and work

    # Regular work with good conditions and low stress
    if alertness >= 0.7 and hypertension <= 0.5 and intoxication <= 0.15:
        return 0  # Just work

    # Default breaks with borderline conditions to prevent issues
    return 3  # Sleep for balance

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)