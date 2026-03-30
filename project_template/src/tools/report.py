import numpy as np
def print_results(np_ages):
    if np_ages is None or len(np_ages) == 0:
        print("No data")
    else:
        print("Statistic info:")
        print(f"Count of friends {len(np_ages)}")
        print(f"The youngest: {np_ages.min()} ")
        print(f"The oldest: {np_ages.max()} ")
        print(f"Mean of age: {np_ages.mean():.1f} ")
        print(f"Median of age: {np.median(np_ages)} ")
        print(f"Sum of all ages: {np_ages.sum()}")
    return print_results

def print_peers(peers, year):
    print(f"\nPeers born in {year}:")
    if not peers:
        print("No peers found.")
    else:
        for p in peers:
            print(f"- {p}")