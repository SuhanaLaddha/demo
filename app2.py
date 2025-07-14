import streamlit as st
import paramiko

st.title("🐳 Simple Remote Docker App")

# SSH Input
rhel_ip = st.text_input("RHEL9 IP Address", "10.167.24.14")
username = st.text_input("SSH Username", "root")
password = st.text_input("SSH Password", type="password")

# Docker Menu
choice = st.selectbox("Choose Docker Option", [
    "1. Launch Container",
    "2. Stop Container",
    "3. Remove Container",
    "4. Start Container",
    "5. List Docker Images",
    "6. List Running Containers",
    "7. Pull Docker Image",
    "8. Exit"
])

# Inputs as per choice
if choice == "1. Launch Container":
    container_name = st.text_input("Enter Container Name")
    image_name = st.text_input("Enter Image Name")
elif choice == "2. Stop Container":
    container_name = st.text_input("Enter Container Name")
elif choice == "3. Remove Container":
    container_name = st.text_input("Enter Container Name")
elif choice == "4. Start Container":
    container_name = st.text_input("Enter Container Name")
elif choice == "7. Pull Docker Image":
    image_name = st.text_input("Enter Image Name")

# On button click
if st.button("Run Docker Command"):

    # Create SSH connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=rhel_ip, username=username, password=password)

    # Choose command
    docker_cmd = ""

    if choice == "1. Launch Container":
        docker_cmd = f"docker run -dit --name {container_name} {image_name}"
    if choice == "2. Stop Container":
        docker_cmd = f"docker stop {container_name}"
    if choice == "3. Remove Container":
        docker_cmd = f"docker rm {container_name}"
    if choice == "4. Start Container":
        docker_cmd = f"docker start {container_name}"
    if choice == "5. List Docker Images":
        docker_cmd = "docker images"
    if choice == "6. List Running Containers":
        docker_cmd = "docker ps"
    if choice == "7. Pull Docker Image":
        docker_cmd = f"docker pull {image_name}"
    if choice == "8. Exit":
        st.warning("Exit selected.")
        st.stop()

    # Run command
    stdin, stdout, stderr = ssh.exec_command(docker_cmd)
    output = stdout.read().decode()
    error = stderr.read().decode()

    # Display output
    if output:
        st.success("Output:")
        st.text(output)
    if error:
        st.error("Error:")
        st.text(error)

    ssh.close()
