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

    # Prioritize sleep based on stricter health conditions
    if hypertension > 0.35 or intoxication > 0.2 or time_since_slept > 8:
        print(3)  # sleep
    # Use coffee to improve alertness effectively when needed
    elif alertness < 0.6 and hypertension < 0.2:
        print(1)  # drink coffee and work
    # Appropriately assess alertness condition for working
    elif alertness >= 0.8 and hypertension < 0.2 and intoxication < 0.05:
        print(0)  # just work
    else:
        print(3)  # default to sleep