import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping if any health-related parameter suggests it
    if (
        alertness < 0.75  # Increased alertness threshold for sleeping
        or time_since_slept >= 3  # Reduced time threshold
        or intoxication > 0.03  # Lower intoxication threshold
        or hypertension > 0.05  # Moderate hypertension consideration
    ):
        return 3  # Opt to sleep for recovery

    # Using coffee carefully to boost and manage alertness
    if alertness < 0.85 and hypertension < 0.02 and time_since_slept < 2.5:
        return 1  # Coffee, but consider health metrics

    # Beer is seldom a safe option; it requires peak conditions
    if alertness > 0.95 and intoxication < 0.01 and hypertension < 0.002:
        return 2  # Use beer only when safe

    return 0  # Default to working if stable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)