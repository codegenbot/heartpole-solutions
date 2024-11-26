import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if any serious health issue
    if hypertension > 0.03 or intoxication > 0.08:
        return 3

    # Sleep if very low alertness, or overdue for sleep
    if alertness < 0.5 or time_since_slept > 7:
        return 3

    # Use beer strategically for moderate hypertension with low intoxication and good alertness
    if 0.02 < hypertension <= 0.03 and intoxication < 0.03 and alertness > 0.7:
        return 2

    # Use coffee when alertness is declining but health metrics are stable
    if alertness < 0.7 and hypertension < 0.02 and intoxication < 0.03:
        return 1

    # Default to work if no immediate health risks
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)