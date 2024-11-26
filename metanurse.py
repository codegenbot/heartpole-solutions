import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate action if serious health concerns
    if hypertension >= 0.01 or intoxication >= 0.03:
        return 3  # Prioritize sleep to mitigate risks

    # Sleep when significantly sleep-deprived or alertness is too low
    if time_since_slept >= 5 or alertness < 0.5:
        return 3  # Ensure recovery with sleep

    # Use coffee to boost alertness if it's moderately low and health allows
    if alertness < 0.6 and hypertension < 0.008 and intoxication < 0.01:
        return 1  # Coffee to improve moderate alertness drop safely

    # Default to work if conditions are within safe range
    return 0  # Focus on productivity if parameters allow

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)