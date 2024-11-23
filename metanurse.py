import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep conditions
    if hypertension > 0.5 or intoxication > 0.5 or alertness < 0.3 or time_since_slept > 16:
        return 3  # Sleep if there's any significant health risk or low alertness

    # Coffee conditions
    if alertness < 0.5 and hypertension <= 0.4 and time_since_slept <= 10:
        return 1  # Drink coffee and work to boost moderate alertness

    # Optimal work conditions
    if alertness >= 0.7 and hypertension < 0.3 and intoxication < 0.2:
        return 0  # Just work if health and alertness are optimal

    # Default to regular work to maintain productivity
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)