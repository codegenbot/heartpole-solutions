import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep when health is at potential risk or alertness is critically low
    if hypertension > 0.03 or intoxication > 0.03 or alertness < 0.25:
        return 3

    # Proactively sleep if it has been too long without sleep
    if time_since_slept > 4 or (alertness < 0.3 and time_since_slept > 2.5):
        return 3

    # Drink coffee if it helps without significant hypertension risk
    if alertness < 0.4 and hypertension < 0.015:
        return 1

    # Maintain balance between work efficacy and alertness
    if alertness >= 0.4 and hypertension < 0.025 and intoxication < 0.02:
        return 0

    # Default to just work if coffee can't be taken and other conditions don't trigger
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)