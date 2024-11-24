import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.7 or intoxication > 0.6:
        return 3  # Prioritize sleep if health parameters are high-risk 
    if time_since_slept > 12:
        return 3  # Mandatory sleep when significantly deprived
    if alertness < 0.5:
        if alertness < 0.3:
            return 3  # Sleep if alertness is critically low
        elif hypertension < 0.6 and intoxication < 0.4:
            return 1  # Coffee to boost alertness, if safe
    if alertness >= 0.6:
        return 0  # Work when alertness is adequately high
    return 2  # Default to beer use cautiously if low alertness persists

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)