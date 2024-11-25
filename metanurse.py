import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if any health indicators are too high or alertness is critically low
    if (
        alertness < 0.3
        or hypertension > 0.08
        or intoxication > 0.05
        or time_since_slept > 4.0
    ):
        return 3  # Sleep to reset health and alertness before things get worse

    # Drink coffee if alertness is moderate, but maintain safe health levels
    if 0.3 <= alertness < 0.6 and hypertension < 0.05 and intoxication < 0.02:
        return 1  # Coffee to boost alertness without crossing health bounds

    # Ideal scenario for just working without stimulants
    if alertness >= 0.6 and hypertension < 0.04 and intoxication < 0.03:
        return 0  # Optimal working conditions: keep going without intervention

    # Use beer only when productivity is low and it's safe health-wise
    if work_done < 0.01 and intoxication <= 0.01 and alertness < 0.35:
        return 2  # Beer if minimal productivity issue, using this sparingly

    # Default action is to work if nothing else is called for
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)