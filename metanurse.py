import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if low alertness or high health risk
    if alertness < 0.5 or hypertension > 0.6 or intoxication > 0.15 or time_since_slept > 4:
        return 3  # Sleep

    # Use coffee to boost alertness at moderate levels with relaxed health conditions
    if alertness < 0.7 and hypertension <= 0.6 and intoxication <= 0.2:
        return 1  # Coffee and work

    # Work under ideal conditions
    if alertness >= 0.65 and hypertension <= 0.5 and intoxication <= 0.1:
        return 0  # Just work

    # Default to just work if non-critical issues are present
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)