import sys

for line in sys.stdin:
    (
        alertness,
        hypertension,
        intoxication,
        time_since_slept,
        time_elapsed,
        work_done,
    ) = map(float, line.split())

    # Prioritize rest more aggressively based on health conditions
    if hypertension > 0.35 or intoxication > 0.18 or time_since_slept > 9:
        print(3)  # sleep
    # Allow coffee consumption under stricter conditions to boost alertness
    elif alertness < 0.4 and hypertension < 0.25 and time_since_slept < 7:
        print(1)  # drink coffee and work
    # Use beer less frequently, ensuring intoxication levels remain manageable
    elif intoxication >= 0.12 and hypertension < 0.3:
        print(2)  # drink beer and work
    # Work normally when all health indicators are good
    elif alertness >= 0.7 and hypertension < 0.25 and intoxication < 0.08:
        print(0)  # just work
    else:
        print(3)  # fallback to sleep if conditions are ambiguous