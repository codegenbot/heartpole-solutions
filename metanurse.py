import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep conditions: handle health-critical situations more aggressively
    if hypertension > 0.4 or intoxication > 0.3 or alertness < 0.4 or time_since_slept > 14:
        return 3  # Sleep if there's any significant health risk or low alertness

    # Coffee conditions: use coffee conservatively with more checks
    if alertness < 0.6 and hypertension <= 0.35 and time_since_slept <= 10 and intoxication < 0.1:
        return 1  # Drink coffee and work to boost moderate alertness

    # Optimal work conditions
    if alertness >= 0.6 and hypertension < 0.25 and intoxication < 0.15:
        return 0  # Just work if health and alertness are optimal

    # Use beer only if minor stress relief is needed
    if alertness >= 0.6 and intoxication < 0.1 and hypertension >= 0.3:
        return 2  # Drink beer and work

    # Default to regular work to maintain productivity
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)