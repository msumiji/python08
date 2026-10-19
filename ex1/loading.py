from importlib import metadata


def check_dependencies() -> bool:
    packages = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
    }

    print("Checking dependencies:")
    missing = []

    for package, description in packages.items():
        try:
            version = metadata.version(package)
            __import__(package)
            print(f"[OK] {package} ({version}) - {description}")
        except (ImportError, metadata.PackageNotFoundError):
            print(f"[ERROR] {package} - Not available")
            missing.append(package)

    if missing:
        print("\nSome dependencies are missing.")
        print("Install them using one of the following:")
        print("pip: python -m pip install -r requirements.txt")
        print("Poetry: poetry install")
        return False

    return True


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")

    if not check_dependencies():
        return
    print()
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("Analyzing Matrix data...")

    # Generate 1000 simulated data points using NumPy
    rng = np.random.default_rng(seed=42)
    matrix = rng.random((10, 10))
    print(f"Processing {matrix.size} data points...")

    # Analyze data using pandas
    df = pd.DataFrame(matrix, columns=[
        f"Column_{i + 1}" for i in range(matrix.shape[1])
    ])
    print("Mean of each column:")

    print("Generating visualization...\n")
    plt.imshow(matrix, aspect="auto")
    plt.colorbar(label="Value")
    plt.title("Matrix Data Analysis")
    plt.xlabel("Column")
    plt.ylabel("Row")
    plt.savefig("matrix_analysis.png")
    plt.close()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
