import sys
from importlib import metadata


def compare_packages() -> None:
    packages = ["numpy", "pandas", "matplotlib"]

    for package in packages:
        try:
            version = metadata.version(package)
            print(f"{package}: {version}")
        except metadata.PackageNotFoundError:
            print(f"{package}: NOT INSTALLED")


def show_package_management() -> None:
    """Explain the differences between pip and Poetry."""
    print("\n=== Dependency Management ===")

    print("pip:")
    print("  Install packages with: pip install -r requirements.txt")
    print("  Dependencies are listed in requirements.txt")

    print("\nPoetry:")
    print("  Install dependencies with: poetry install")
    print("  Dependencies are listed in pyproject.toml")
    print("  poetry.lock records resolved dependency versions")


def main() -> None:
    print("=== MATRIX DATA ANALYSIS ===")

    # Handle missing external dependencies
    try:
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
    except ImportError as error:
        print(f"ERROR: Missing dependency: {error.name}")
        print("Install dependencies using pip or Poetry.")
        print("pip: pip install -r requirements.txt")
        print("Poetry: poetry install")
        return

    # Generate simulated Matrix data using NumPy
    rng = np.random.default_rng(seed=42)

    data = rng.normal(loc=100, scale=15, size=(10, 3))

    # Use pandas to organize and analyze the data
    df = pd.DataFrame(
        data,
        columns=["Red Pill", "Blue Pill", "Green Pill"],
    )

    print("\n--- Simulated Matrix Data ---")
    print(df.round(2))

    print("\n--- Statistical Analysis ---")
    print(df.describe().round(2))

    # Visualize the data using Matplotlib
    df.plot(
        kind="line",
        marker="o",
        title="Matrix Data Simulation",
    )
    plt.xlabel("Simulation Step")
    plt.ylabel("Matrix Value")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("matrix_data.png")
    print("\nGraph saved as matrix_data.png")

    # Compare installed package versions
    compare_packages()

    # Explain pip and Poetry
    show_package_management()

    print("\nSUCCESS: Matrix data analysis complete!")


if __name__ == "__main__":
    main()
