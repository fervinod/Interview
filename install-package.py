import paramiko
from concurrent.futures import ThreadPoolExecutor

# -----------------------------
# CONFIGURATION
# -----------------------------

HOSTS = [
    "10.0.0.11",
    "10.0.0.12",
    "10.0.0.13"
]

USERNAME = "ubuntu"
PASSWORD = "your_password"

PACKAGE_NAME = "nginx"

# -----------------------------
# SSH FUNCTION
# -----------------------------

def install_and_check(host):
    print(f"\n[+] Connecting to {host}")

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(
            hostname=host,
            username=USERNAME,
            password=PASSWORD,
            timeout=10
        )

        # Detect package manager
        stdin, stdout, stderr = client.exec_command(
            "which apt && echo apt || which yum && echo yum"
        )

        package_manager = stdout.read().decode().strip().split("\n")[-1]

        print(f"[{host}] Package manager: {package_manager}")

        # Install package
        if package_manager == "apt":
            install_cmd = f"sudo apt update -y && sudo apt install -y {PACKAGE_NAME}"
            version_cmd = f"dpkg -s {PACKAGE_NAME} | grep Version"

        elif package_manager == "yum":
            install_cmd = f"sudo yum install -y {PACKAGE_NAME}"
            version_cmd = f"rpm -qi {PACKAGE_NAME} | grep Version"

        else:
            print(f"[{host}] Unsupported package manager")
            return

        print(f"[{host}] Installing package...")

        stdin, stdout, stderr = client.exec_command(install_cmd)

        exit_status = stdout.channel.recv_exit_status()

        if exit_status == 0:
            print(f"[{host}] Installation successful")
        else:
            print(f"[{host}] Installation failed")
            print(stderr.read().decode())
            return

        # Get package version
        stdin, stdout, stderr = client.exec_command(version_cmd)

        version_output = stdout.read().decode().strip()

        print(f"[{host}] Installed version:")
        print(version_output)

    except Exception as e:
        print(f"[{host}] ERROR: {e}")

    finally:
        client.close()


# -----------------------------
# MAIN
# -----------------------------

with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(install_and_check, HOSTS)