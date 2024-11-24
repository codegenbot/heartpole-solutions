import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if very low alertness or health issues
    if alertness < 0.5 or hypertension > 0.6 or intoxication > 0.3 or time_since_slept > 6:
        return 3  # Sleep if any health indicator is concerning

    # Coffee to boost alertness and productivity
    if 0.5 <= alertness < 0.8 and hypertension <= 0.5 and intoxication <= 0.15:
        return 1  # Use coffee if alertness is moderate and health is stable

    # Optimal work condition
    if alertness >= 0.8 and hypertension <= 0.4 and intoxication <= 0.1:
        return 0  # Work if alertness is high and health is optimal

    # Use beer cautiously under low risk
    if intoxication < 0.15 and hypertension <= 0.4:
        return 2  # Beer only when health risks are minimal

    # Default to sleep as the safest choice
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)