import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.7 or intoxication > 0.7:
        return 3  # Sleep if high health risks
    if time_since_slept > 14:
        return 3  # Ensure sleep if excessively deprived

    if alertness < 0.4:
        return 3  # Mandatory sleep if alertness is very low
    elif alertness < 0.6:
        if hypertension < 0.6 and intoxication < 0.5:
            return 1  # Coffee to boost alertness safely
        else:
            return 3  # Sleep if conditions are unsafe for coffee

    if alertness >= 0.7 and hypertension <= 0.5:
        return 0  # Work efficiently with high alertness and low hypertension
    return 2  # Conservative beer use when alertness is moderate

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)