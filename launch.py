
from waser import WASER

def main():
    """
    Example usage of the Spectral Wasserstein Distance
    """

    # Initialize the distance calculator
    waser_r1 = WASER(k=100, method='r1')
    waser_r_multi = WASER(k=100, method='r_multi')

    # Compute distances
    print("Computing Spectral Wasserstein Distance (r=1 method)...")
    distance_r1 = waser_r1.compute_distance_from_files("path/to/your/first/file.vec", "path/to/your/second/file.vec")
    print(f"Distance (r=1): {distance_r1:.6f}")

    print("\nComputing Spectral Wasserstein Distance (r>1 method)...")
    distance_r_multi = waser_r_multi.compute_distance_from_files("path/to/your/first/file.vec", "path/to/your/second/file.vec")
    print(f"Distance (r>1): {distance_r_multi:.6f}")

    # Example with custom file paths
    print("\n" + "=" * 50)



if __name__ == "__main__":
    main()
