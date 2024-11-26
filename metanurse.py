import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep when necessary
    if time_since_slept >= 2.5 or alertness < 0.5:
        return 3  # Sleep

    # Avoid hypertension or intoxication
    if hypertension > 0.05 or intoxication > 0.04:
        return 3  # Sleep to recover health

    # Use coffee to boost alertness only when safe
    if alertness >= 0.5 and alertness < 0.7 and hypertension < 0.04:
        return 1  # Coffee and work

    # Work efficiently when conditions are optimal
    if alertness >= 0.7 and hypertension < 0.03 and intoxication < 0.02:
        return 0  # Just work

    # Use beer in strict conditions for motivation, but prioritize sleep
    if work_done < 0.01 and intoxication <= 0.01 and alertness < 0.3:
        return 2  # Beer and work

    return 0  # Default to just work if no other conditions apply

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)