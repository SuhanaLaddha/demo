import streamlit as st
import os

st.title(" Docker Management Dashboard")
st.write("Select an action below:")

option = st.selectbox("Choose an action", [
    "Launch Container",
    "Stop Container",
    "Remove Container",
    "Start Container",
    "List Docker Images",
    "List Containers",
    "Pull Image from Docker Hub",
    "Exit"
])


if option == "Launch Container":
    name = st.text_input("Container name")
    image = st.text_input("Image name (e.g., ubuntu)")
    if st.button("Launch"):
        if name and image:
            out, err, code = run_command(f"docker run -dit --name {name} {image}")
            if code == 0:
                st.success(f"Container '{name}' launched.")
            else:
                st.error(err)
        else:
            st.warning("Enter both name and image.")

elif option == "Stop Container":
    name = st.text_input("Container name to stop")
    if st.button("Stop"):
        out, err, code = run_command(f"docker stop {name}")
        if code == 0:
            st.success(f"Stopped '{name}'.")
        else:
            st.error(err)

elif option == "Remove Container":
    name = st.text_input("Container name to remove")
    if st.button("Remove"):
        out, err, code = run_command(f"docker rm -f {name}")
        if code == 0:
            st.success(f"Removed '{name}'.")
        else:
            st.error(err)

elif option == "Start Container":
    name = st.text_input("Container name to start")
    if st.button("Start"):
        out, err, code = run_command(f"docker start {name}")
        if code == 0:
            st.success(f"Started '{name}'.")
        else:
            st.error(err)

elif option == "List Docker Images":
    if st.button("Show Images"):
        out, _, _ = run_command("docker images")
        st.text_area("Images", out, height=300)

elif option == "List Containers":
    if st.button("Show Containers"):
        out, _, _ = run_command("docker ps -a")
        st.text_area("Containers", out, height=300)

elif option == "Pull Image from Docker Hub":
    image = st.text_input("Image name (e.g., nginx:latest)")
    if st.button("Pull"):
        out, err, code = run_command(f"docker pull {image}")
        if code == 0:
            st.success(f"Image '{image}' pulled successfully.")
            st.text(out)
        else:
            st.error(err)

elif option == "Exit":
    st.info("You may now close this browser tab or stop the app.")



