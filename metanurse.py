import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if health metrics are beyond thresholds or sleep-deprived
    if hypertension > 0.32 or intoxication > 0.2 or time_since_slept > 6.5 or alertness < 0.5:
        return 3  # Sleep

    # Drink coffee if moderate alertness to boost productivity, only when stable
    if 0.5 <= alertness < 0.75 and hypertension < 0.3 and intoxication < 0.1:
        return 1  # Drink coffee and work

    # Avoid actions involving coffee or beer if health is borderline
    if 0.3 <= hypertension <= 0.36 or 0.15 <= intoxication <= 0.25:
        return 0  # Just work to stabilize

    # Drink beer might not be beneficial due to intoxication, avoid it broadly
    # Focus on reducing risk of further intoxication.

    # Default to working if no health metric indicates immediate risk 
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)