import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate action if serious health concerns
    if hypertension > 0.012 or intoxication > 0.045:
        return 3  # Prioritize sleep to mitigate risks

    # Sleep when significantly sleep-deprived or alertness is too low
    if time_since_slept > 6 or alertness < 0.5:
        return 3  # Ensure recovery with sleep

    # Use coffee to boost alertness safely if below optimal but healthy
    if alertness < 0.8 and hypertension < 0.012 and intoxication < 0.02:
        return 1  # Coffee to enhance safe productivity

    # Consider beer to relax if hypertension permits
    if intoxication < 0.025 and hypertension < 0.008:
        return 2  # Beer to reduce stress if health allows

    # Default to work
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)