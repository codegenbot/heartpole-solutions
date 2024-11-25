import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate response to critical health metrics
    if hypertension > 0.16 or intoxication > 0.16 or time_since_slept > 5:
        return 3  # sleep to tackle serious issues

    # Sleep if severely lacking alertness
    if alertness < 0.65:
        return 3

    # Use coffee only if safe from high hypertension and requiring alertness
    if alertness < 0.8 and hypertension < 0.1:
        return 1  # boost alertness safely

    # Ideal working conditions
    if alertness >= 0.85 and hypertension < 0.08 and intoxication < 0.05:
        return 0  # continue working efficiently

    # Relax conditionally when workload is significantly lower
    if work_done < 0.55 and intoxication < 0.08:
        return 2  # mild relaxation with beer

    return 0  # default to just work when other conditions are stable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)