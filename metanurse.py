import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate action if serious health concerns
    if hypertension > 0.015 or intoxication > 0.05:
        return 3  # Sleep to mitigate health risks

    # Sleep when significantly sleep-deprived or alertness is too low
    if time_since_slept > 6 or alertness < 0.4:
        return 3  # Recovery with sleep

    # Use coffee to boost alertness safely if below optimal but healthy
    if alertness < 0.75 and hypertension < 0.015 and intoxication < 0.02:
        return 1  # Coffee to enhance productivity safely

    # Consider beer to relax if hypertension and intoxication permit
    if intoxication < 0.03 and hypertension < 0.01:
        return 2  # Beer for stress relief

    # Default to work
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)