import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if any condition is suboptimal for health or alertness
    if alertness < 0.4 or hypertension > 0.75 or intoxication > 0.45 or time_since_slept > 10:
        return 3  # Need sleep

    # Optimal work condition
    if alertness > 0.8 and hypertension < 0.6 and intoxication < 0.1:
        return 0  # Just work

    # Coffee to boost when moderately alert but safe
    if 0.5 <= alertness <= 0.8 and hypertension < 0.6 and intoxication < 0.15:
        return 1  # Coffee and work

    # Use beer only in balanced conditions to slightly improve morale and work
    if alertness < 0.5 and hypertension < 0.45 and intoxication < 0.1:
        return 2  # Beer and work

    # Default to sleep
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)