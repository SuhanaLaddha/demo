import streamlit as st
import paramiko

st.title("Remote RHEL Linux + Docker Dashboard (via SSH)")

# --- SSH credentials input ---
host = st.text_input("Enter RHEL IP address", value="192.168.1.100")
username = st.text_input("Enter username", value="root")
password = st.text_input("Enter password", type="password")

# --- Linux command menu ---
menu = [
    "1: Show current date",
    "2: Show calendar",
    "3: Show current user",
    "4: Print working directory",
    "5: List files in current directory",
    "6: List all files with details",
    "7: Show disk usage",
    "8: Show memory usage",
    "9: Show CPU info",
    "10: Show kernel version",
    "11: Show OS details",
    "12: List USB devices",
    "13: List PCI devices",
    "14: List block devices",
    "15: List network interfaces",
    "16: Check internet connectivity (ping)",
    "17: Show IP address",
    "18: Show open ports",
    "19: Show active processes",
    "20: Search running process by name",
    "21: Kill a process by PID",
    "22: Create a new directory",
    "23: Remove a directory",
    "24: Create a new file",
    "25: Remove a file",
    "26: Copy a file",
    "27: Move (rename) a file",
    "28: Change file permissions",
    "29: Change file ownership",
    "30: Archive files using tar",
    "31: Extract tar archive",
    "32: Find a file by name",
    "33: Show environment variables",
    "34: Echo a message",
    "35: Shutdown system",
    "36: Reboot system",
    "37: List users",
    "38: List logged in users",
    "39: Show last login info",
    "40: Clear the screen",
    "41: Check system uptime",
    "42: Show hostname",
    "43: Change hostname",
    "44: Update software packages (dnf)",
    "45: Install a package (dnf)",
    "46: Remove a package (dnf)",
    "47: Check Docker version",
    "48: List Docker containers",
    "49: List Docker images",
    "50: Exit"
]

# Split into categories for usability
system_commands = [
    "1: Show current date",
    "2: Show calendar",
    "3: Show current user",
    "4: Print working directory",
    "5: List files in current directory",
    "6: List all files with details",
    "7: Show disk usage",
    "8: Show memory usage",
    "9: Show CPU info",
    "10: Show kernel version"
]

docker_commands = [
    "47: Check Docker version",
    "48: List Docker containers",
    "49: List Docker images"
]

file_commands = [
    "22: Create a new directory",
    "24: Create a new file",
    "25: Remove a file",
    "26: Copy a file",
    "27: Move (rename) a file",
    "28: Change file permissions",
    "29: Change file ownership",
    "30: Archive files using tar",
    "31: Extract tar archive"
]

st.subheader("🖥️ System Commands")
selected = st.radio("Choose a system command", system_commands)

st.subheader("📁 File Commands")
if st.checkbox("Show file commands"):
    selected = st.radio("Choose a file command", file_commands, key="file_cmd")

st.subheader("🐳 Docker Commands")
if st.checkbox("Show Docker commands"):
    selected = st.radio("Choose a Docker command", docker_commands, key="docker_cmd")

run = st.button("Connect and Execute")


# --- Run command via SSH ---
if run:
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=username, password=password)

        command = ""

        # Logic for each option
        if selected.startswith("1"):
            command = "date"
        elif selected.startswith("2"):
            command = "cal"
        elif selected.startswith("3"):
            command = "whoami"
        elif selected.startswith("4"):
            command = "pwd"
        elif selected.startswith("5"):
            command = "ls"
        elif selected.startswith("6"):
            command = "ls -l"
        elif selected.startswith("7"):
            command = "df -h"
        elif selected.startswith("8"):
            command = "free -h"
        elif selected.startswith("9"):
            command = "lscpu"
        elif selected.startswith("10"):
            command = "uname -r"
        elif selected.startswith("11"):
            command = "cat /etc/os-release"
        elif selected.startswith("12"):
            command = "lsusb"
        elif selected.startswith("13"):
            command = "lspci"
        elif selected.startswith("14"):
            command = "lsblk"
        elif selected.startswith("15"):
            command = "ip link show"
        elif selected.startswith("16"):
            command = "ping -c 4 google.com"
        elif selected.startswith("17"):
            command = "ip a"
        elif selected.startswith("18"):
            command = "ss -tuln"
        elif selected.startswith("19"):
            command = "top -n 1 -b"
        elif selected.startswith("20"):
            pname = st.text_input("Enter process name to search:")
            if pname: command = f"ps aux | grep {pname}"
        elif selected.startswith("21"):
            pid = st.text_input("Enter PID to kill:")
            if pid: command = f"kill {pid}"
        elif selected.startswith("22"):
            dirname = st.text_input("Enter directory name to create:")
            if dirname: command = f"mkdir {dirname}"
        elif selected.startswith("23"):
            dirname = st.text_input("Enter directory name to remove:")
            if dirname: command = f"rmdir {dirname}"
        elif selected.startswith("24"):
            filename = st.text_input("Enter file name to create:")
            if filename: command = f"touch {filename}"
        elif selected.startswith("25"):
            filename = st.text_input("Enter file name to delete:")
            if filename: command = f"rm {filename}"
        elif selected.startswith("26"):
            src = st.text_input("Enter source file:")
            dest = st.text_input("Enter destination path:")
            if src and dest: command = f"cp {src} {dest}"
        elif selected.startswith("27"):
            src = st.text_input("Enter file to move/rename:")
            dest = st.text_input("Enter new location or name:")
            if src and dest: command = f"mv {src} {dest}"
        elif selected.startswith("28"):
            file = st.text_input("Enter file name:")
            perms = st.text_input("Enter permissions (e.g., 755):")
            if file and perms: command = f"chmod {perms} {file}"
        elif selected.startswith("29"):
            file = st.text_input("Enter file name:")
            owner = st.text_input("Enter new owner:")
            if file and owner: command = f"chown {owner} {file}"
        elif selected.startswith("30"):
            name = st.text_input("Enter archive name (e.g., archive.tar):")
            files = st.text_input("Enter files to archive (space-separated):")
            if name and files: command = f"tar -cvf {name} {files}"
        elif selected.startswith("31"):
            archive = st.text_input("Enter archive file to extract:")
            if archive: command = f"tar -xvf {archive}"
        elif selected.startswith("32"):
            fname = st.text_input("Enter file name to search:")
            if fname: command = f"find / -name {fname} 2>/dev/null"
        elif selected.startswith("33"):
            command = "printenv"
        elif selected.startswith("34"):
            msg = st.text_input("Enter message to echo:")
            if msg: command = f"echo {msg}"
        elif selected.startswith("35"):
            command = "shutdown now"
        elif selected.startswith("36"):
            command = "reboot"
        elif selected.startswith("37"):
            command = "cut -d: -f1 /etc/passwd"
        elif selected.startswith("38"):
            command = "who"
        elif selected.startswith("39"):
            command = "last"
        elif selected.startswith("40"):
            command = "clear"
        elif selected.startswith("41"):
            command = "uptime"
        elif selected.startswith("42"):
            command = "hostname"
        elif selected.startswith("43"):
            new_name = st.text_input("Enter new hostname:")
            if new_name: command = f"hostnamectl set-hostname {new_name}"
        elif selected.startswith("44"):
            command = "sudo dnf update -y"
        elif selected.startswith("45"):
            pkg = st.text_input("Enter package name to install:")
            if pkg: command = f"sudo dnf install {pkg} -y"
        elif selected.startswith("46"):
            pkg = st.text_input("Enter package name to remove:")
            if pkg: command = f"sudo dnf remove {pkg} -y"
        elif selected.startswith("47"):
            command = "docker version"
        elif selected.startswith("48"):
            command = "docker ps -a"
        elif selected.startswith("49"):
            command = "docker images"
        elif selected.startswith("50"):
            st.success("Goodbye! You can close the app.")
            ssh.close()
            st.stop()
        else:
            command = "echo Invalid choice"

        # Run command if ready
        if command:
            stdin, stdout, stderr = ssh.exec_command(command)
            result = stdout.read().decode().strip()
            error = stderr.read().decode().strip()

            if result:
                st.text_area("Output", result, height=300)
            elif error:
                st.text_area("Error", error, height=200)
            else:
                st.success("✅ Command executed successfully (no output returned)")

        ssh.close()

    except Exception as e:
        st.error(f"❌ SSH Connection Failed: {e}")



