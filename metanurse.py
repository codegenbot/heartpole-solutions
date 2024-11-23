import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep on low alertness or high time since slept
    if alertness < 0.35 or time_since_slept > 8:
        return 3  # Sleep

    # Avoid drinking if near health risk levels
    if hypertension >= 0.2 or intoxication >= 0.2:
        return 3  # Sleep if close to health issues

    # Use coffee only to boost alertness when it's safe
    if alertness < 0.6 and hypertension < 0.15:
        return 1  # Drink coffee and work

    # Prefer working when alertness is sufficient
    if alertness >= 0.7:
        return 0  # Just work

    return 0  # Default to just work more often

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)