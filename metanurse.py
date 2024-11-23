import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep when extremely tired or on risk of health
    if alertness < 0.4 or time_since_slept >= 6 or hypertension >= 0.3 or intoxication >= 0.25:
        return 3  # Sleep

    # If slightly tired or need an alertness boost
    if alertness < 0.7:
        return 1  # Drink coffee and work

    # Allow beer only when all conditions are favorable and alertness is high
    if alertness >= 0.8 and intoxication < 0.05 and hypertension < 0.15:
        return 2  # Drink beer and work

    # If everything else is fine, just work
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)