import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep conditions
    if (
        hypertension > 0.6 or intoxication > 0.4 or alertness < 0.3 or 
        time_since_slept >= 14
    ):
        return 3  # Sleep if significantly risky or very low alertness

    # Beer for stress relief if lightly intoxicated and time_since_slept substantial
    if intoxication < 0.3 and hypertension > 0.4 and time_since_slept > 10:
        return 2  # Drink beer to reduce hypertension effects

    # Coffee conditions
    if alertness < 0.5 and hypertension <= 0.4:
        return 1  # Drink coffee to boost alertness

    # Optimal work conditions
    if alertness >= 0.6 and hypertension < 0.3 and intoxication <= 0.2:
        return 0  # Just work if health and alertness are optimal

    # Default: if no urgent health risk, just work
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)