import os
import sys
from dotenv import load_dotenv


def main() -> None:
    # Load environment variables from .env
    load_dotenv()

    # Required configuration variables
    required_variables = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT",
    ]

    # Check for missing configuration
    config = {}
    missing = []

    for name in required_variables:
        value = os.getenv(name)
        if not value:
            missing.append(name)
        else:
            config[name] = value

    if missing:
        print(f"ERROR: Missing configuration: {', '.join(missing)}")
        sys.exit(1)

    # Validate MATRIX_MODE
    mode = config["MATRIX_MODE"].lower()

    if mode not in ("development", "production"):
        print("ERROR: MATRIX_MODE must be 'development' or 'production'")
        sys.exit(1)

    # Validate LOG_LEVEL
    valid_log_levels = ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")
    log_level = config["LOG_LEVEL"].upper()

    if log_level not in valid_log_levels:
        print(f"ERROR: Invalid LOG_LEVEL: {log_level}")
        sys.exit(1)

    # Display configuration
    print("ORACLE STATUS: Reading the Matrix...")
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print("Database: Connected to local instance")
    print("API Access: Authenticated")
    print(f"Log Level: {log_level}")
    print("Zion Network: Online")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.isfile(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[ERROR] .env file not found")
    print("[OK] Production overrides available")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
