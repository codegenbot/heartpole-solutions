import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if multiple critical health indicators are present
    if hypertension > 0.6 or intoxication > 0.4 or alertness < 0.3 or time_since_slept > 8:
        return 3  # Sleep
    # Use coffee to keep alertness and productivity high with moderate safe levels
    if alertness < 0.5 and hypertension < 0.4 and intoxication < 0.2:
        return 1  # Drink coffee and work
    # Opt for work if the user can afford moderate intoxication effects and needs alertness.
    if 0.15 < intoxication < 0.3 and hypertension < 0.5 and alertness > 0.6:
        return 2  # Drink beer and work
    return 0  # Default to just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)