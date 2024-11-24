import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.5 or time_since_slept > 8 or hypertension > 0.7 or intoxication > 0.4:
        return 3  # Prioritize sleep
    if alertness < 0.7 and hypertension <= 0.6 and intoxication <= 0.3:
        return 1  # Coffee to boost alertness
    if alertness >= 0.7 and hypertension < 0.5 and intoxication < 0.2:
        return 0  # Just work
    return 2  # Resort to beer as a fallback if mild intoxication & alertness drop

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)