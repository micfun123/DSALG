# Collisions are inevitable when mapping many keys to fewer hash values.
# Modulo Hashing uses the operation h(k) = k mod m, mapping key k to a hash
# value with modulus m. Hash 100 random and unique integer keys with
# different values of m and compare the distribution and collision rates across
# multiple trials.


"""
Run an experiment of modulo hashing collisions.

Generates `num_keys` unique integer keys (by default 100) and, for each
modulus `m` in a list, repeats `trials` independent trials computing the
number of collisions under `h(k) = k mod m`.

Outputs average and standard deviation of collisions per `m`. Optionally
plots the average collisions vs m if `matplotlib` is available or if the
`--plot` flag is provided.
"""

import argparse
import random
from collections import defaultdict
import statistics
import sys


def modulo_hash(key, m):
    return key % m


def run_trial(keys, m):
    """Compute collisions for one trial with given keys and modulus m.

    Returns the number of collisions (i.e., keys that map to already used
    buckets). Equivalent to num_keys - number_of_occupied_buckets.
    """
    seen = set()
    collisions = 0
    for k in keys:
        h = modulo_hash(k, m)
        if h in seen:
            collisions += 1
        else:
            seen.add(h)
    return collisions


def experiment(num_keys=100, m_values=None, trials=200, key_range=10000, seed=None):
    if m_values is None:
        # test a range of m that are smaller, about equal to, and larger than num_keys
        m_values = [50, 75, 100, 128, 150, 200, 300]

    if seed is not None:
        random.seed(seed)

    results = {}

    for m in m_values:
        trial_collisions = []
        for _ in range(trials):
            # sample unique keys for this trial
            keys = random.sample(range(key_range), num_keys)
            c = run_trial(keys, m)
            trial_collisions.append(c)

        avg = statistics.mean(trial_collisions)
        stdev = statistics.pstdev(trial_collisions)
        results[m] = {
            "avg_collisions": avg,
            "stddev_collisions": stdev,
            "all": trial_collisions,
        }

    return results


def print_results(results, num_keys, trials):
    print(f"Experiment: {num_keys} unique keys, {trials} trials per m")
    print("m\tavg_collisions\tstddev")
    for m in sorted(results.keys()):
        r = results[m]
        print(f"{m}\t{r['avg_collisions']:.3f}\t	{r['stddev_collisions']:.3f}")


def try_plot(results):
    try:
        import matplotlib.pyplot as plt
    except Exception:
        print("matplotlib not available; skipping plot")
        return

    ms = sorted(results.keys())
    avgs = [results[m]["avg_collisions"] for m in ms]

    plt.figure(figsize=(8, 4))
    plt.plot(ms, avgs, marker="o")
    plt.title("Average collisions vs modulus m")
    plt.xlabel("m (number of buckets)")
    plt.ylabel("Average collisions (out of num_keys)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main(argv=None):
    parser = argparse.ArgumentParser(description="Modulo hashing collision experiment")
    parser.add_argument("--keys", type=int, default=100, help="number of unique keys per trial")
    parser.add_argument("--trials", type=int, default=200, help="number of trials per m")
    parser.add_argument("--m", type=int, nargs="*", help="list of m values to test")
    parser.add_argument("--range", type=int, default=10000, help="range to draw random keys from (0..range-1)")
    parser.add_argument("--seed", type=int, default=None, help="random seed for reproducibility")
    parser.add_argument("--plot", action="store_true", help="show plot of average collisions vs m if matplotlib is available")

    args = parser.parse_args(argv)

    results = experiment(num_keys=args.keys, m_values=args.m, trials=args.trials, key_range=args.range, seed=args.seed)
    print_results(results, args.keys, args.trials)
    if args.plot:
        try_plot(results)


if __name__ == "__main__":
    main()



