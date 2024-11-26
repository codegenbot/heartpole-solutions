import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if risks exceed optimal thresholds
    if hypertension > 0.02 or intoxication > 0.08:
        return 3  # Immediate sleep to address urgent health risks

    # Sleep if lack of sleep or severe alertness drop
    if time_since_slept > 6 or alertness < 0.5:
        return 3  # Sleep to recover

    # Use coffee to improve alertness when safe
    if alertness < 0.6 and hypertension < 0.015 and intoxication < 0.03:
        return 1  # Coffee to boost alertness safely

    # Default to work if alertness is adequate
    return 0  # Directly proceed to work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)