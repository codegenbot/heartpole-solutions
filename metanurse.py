import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # If any critical condition exists, prioritize sleep
    if alertness < 0.3 or hypertension > 0.8 or intoxication > 0.5 or time_since_slept > 12:
        return 3  # Need sleep

    # Optimal condition just for work
    if alertness > 0.8 and hypertension < 0.6 and intoxication < 0.2:
        return 0  # Just work

    # Use coffee to maintain productivity if tired but not critical
    if 0.5 <= alertness < 0.8 and hypertension < 0.7 and intoxication < 0.3 and time_since_slept <= 8:
        return 1  # Coffee and work

    # Utilize beer to stabilize if alertness is low and no immediate sleep need
    if alertness < 0.5 and hypertension < 0.5 and intoxication < 0.3 and time_since_slept <= 10:
        return 2  # Beer and work

    # Default to cautious approach; favor sleep when approaching risky conditions
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)