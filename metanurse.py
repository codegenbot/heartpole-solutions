import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Check severe hypertension and intoxication:
    if hypertension > 0.05 or intoxication > 0.05:
        return 3  # Sleep to address severe health issues

    # Sleep if not slept recently or for minor hypertension/intoxication:
    if time_since_slept > 6 or hypertension > 0.03 or intoxication > 0.04:
        return 3

    # Use coffee to maintain good alertness unless health conditions are worsening:
    if alertness < 0.6 and hypertension < 0.025 and intoxication < 0.02:
        return 1

    # Work only if alertness and health conditions are optimal:
    if alertness >= 0.8 and hypertension < 0.01 and intoxication < 0.01:
        return 0

    # Default action, lightly drinking beer to manage moderate alertness drop:
    if alertness < 0.7 and intoxication < 0.03:
        return 2

    # Otherwise, default to sleeping:
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)