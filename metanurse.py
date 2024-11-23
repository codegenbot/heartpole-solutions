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

    # Health comes first: stricter thresholds for sleep or intoxication management
    if hypertension > 0.4 or intoxication > 0.2 or time_since_slept > 10:
        print(3)  # sleep
    # If alertness is low and health allows, consider coffee for productivity
    elif alertness < 0.5 and hypertension < 0.3 and time_since_slept < 8:
        print(1)  # drink coffee and work
    # Use beer to address levels of intoxication and hypertension specifically
    elif intoxication >= 0.15:
        print(2)  # drink beer and work
    # Safest to work when all health factors are optimal
    elif alertness >= 0.6 and hypertension < 0.3 and intoxication < 0.1:
        print(0)  # just work
    else:
        print(3)  # fallback to sleep if conditions are ambiguous