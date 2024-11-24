import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Adjusted thresholds for health risks
    if hypertension > 0.6 or intoxication > 0.55:
        return 3  # Sleep if health risks are above adjusted thresholds

    if time_since_slept > 10:
        return 3  # Adjust to ensure more frequent sleep

    if alertness < 0.4:
        return 3  # Mandatory sleep when alertness is very low

    if alertness < 0.6:
        if hypertension < 0.5 and intoxication < 0.4:
            return 1  # Coffee to safely boost alertness
        else:
            return 3  # Sleep due to unsafe conditions for stimulants

    if alertness >= 0.7 and hypertension < 0.5:
        return 0  # Work efficiently

    return 2  # Use beer cautiously when alertness is moderate

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)