import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize health conditions more carefully
    if hypertension > 0.05 or intoxication > 0.15:
        return 3  # Sleep to address health warnings

    # If very low alertness or serious lack of sleep, prioritize sleep
    if alertness < 0.4 or time_since_slept > 8:
        return 3  # Sleep

    # Use coffee to boost medium alertness, ensuring health is stable
    if 0.4 <= alertness < 0.6 and hypertension < 0.03:
        return 1  # Coffee and work

    # Opt to work if conditions are stable and alertness is reasonable
    if alertness >= 0.6 and intoxication < 0.1:
        return 0  # Work safely without coffee

    # Consider small beer intake if alertness is dropping, but otherwise healthy
    if 0.3 <= alertness < 0.4 and intoxication < 0.05 and hypertension < 0.02:
        return 2  # Beer and work

    return 3  # Favor sleep otherwise

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)