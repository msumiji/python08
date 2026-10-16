import os
import sys
import site


def main():
    in_venv = sys.prefix != sys.base_prefix

    if in_venv:
        env_path = sys.prefix
        env_name = os.path.basename(env_path)
        print("MATRIX STATUS: Welcome to the construct\n")
        print("Current Python:", sys.executable)
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {env_path}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")
        print("Package installation path:")
        print(site.getsitepackages()[0])

    else:
        print("MATRIX STATUS: You're still plugged in\n")
        print("Current Python:", sys.executable)
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machine can see everything you install.\n")
        print("To enter the constract, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\Scripts\activate # On Windows\n")
        print("Then run this program again.")


if __name__ == "__main__":
    main()
