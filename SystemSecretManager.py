import subprocess
import sys
import os

def secret_default_vault(secret_string):
    """
    Fetch secret using default password store.
    """
    try:
        process_cmd = f"pass {secret_string}"
        process = subprocess.run(["bash", "-c", process_cmd], capture_output=True, text=True)
        if process.returncode == 0:
            sec = process.stdout.strip()
            return sec if sec else None
    except Exception as e:
        print(f"ERROR: {str(e)}")
    return None

def secret_custom_vault(secret_path, secrets_dir):
    try:
        env = os.environ.copy()
        env["PASSWORD_STORE_DIR"] = secrets_dir
        process = subprocess.run(
            ["pass", secret_path],
            capture_output=True,
            text=True,
            env=env
        )
        if process.returncode == 0:
            sec = process.stdout.strip()
            return sec if sec else None
    except Exception as e:
        print(f"Error: {str(e)}")
    return None

def main():
    args = sys.argv[1:]
    if len(args) == 0 or len(args) > 2:
        print("Usage: python system_secret_manager.py <secret/path> [<secrets_dir>]", file=sys.stderr)
        sys.exit(1)

    secret_path = args[0]

    if len(args) == 2:
        secrets_dir = args[1]
        secret_value = secret_custom_vault(secret_path, secrets_dir)
    else:
        secret_value = secret_default_vault(secret_path)

    if secret_value:
        print(secret_value)
    else:
        print("No secret!")

if __name__ == "__main__":
    main()

