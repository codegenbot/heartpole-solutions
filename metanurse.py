import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.5 or intoxication > 0.3 or time_since_slept >= 10:
        return 3  # Prioritize sleeping for high hypertension or intoxication
    if alertness < 0.5:
        return 3  # Sleep if alertness is critically low
    if hypertension > 0.3 or intoxication > 0.15:
        return 3  # Sleep if health metrics exceed moderate thresholds
    if alertness < 0.7 and hypertension < 0.3 and intoxication < 0.1:
        return 1  # Coffee to boost alertness if conditions allow
    if alertness > 0.85 and intoxication <= 0.05 and hypertension < 0.15:
        return 2  # Beer in optimal conditions
    return 0  # Just work if everything is stable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)