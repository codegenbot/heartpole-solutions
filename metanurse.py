import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.5 or intoxication > 0.25 or alertness < 0.5 or time_since_slept >= 8:
        return 3  # Prioritize sleep immediately if health indicators are concerning
    if alertness < 0.7 and hypertension < 0.35 and intoxication < 0.2:
        return 1  # Use coffee more conservatively
    if 0.15 < intoxication < 0.3 and hypertension < 0.45 and alertness > 0.6:
        return 2  # Allow beer only if conditions are mild
    return 0  # Default to work if all indicators suggest stability

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)