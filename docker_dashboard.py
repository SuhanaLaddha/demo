import streamlit as st
import docker

# Connect to Docker
client = docker.from_env()

st.title("🐳 Docker Dashboard")

# Action options
action = st.selectbox("Select an action:", [
    "List Containers",
    "List Images",
    "Start Container",
    "Stop Container",
    "Remove Container",
    "Launch New Container",
    "Pull Docker Image"
])

# List all containers
if action == "List Containers":
    containers = client.containers.list(all=True)
    if containers:
        for c in containers:
            st.write(f"📦 Name: {c.name}, Status: {c.status}, ID: {c.short_id}")
    else:
        st.info("No containers found.")

# List all images
elif action == "List Images":
    images = client.images.list()
    if images:
        for img in images:
            st.write(f"🖼️ {img.tags}")
    else:
        st.info("No images found.")

# Start a container
elif action == "Start Container":
    name = st.text_input("Enter container name to start")
    if st.button("Start"):
        try:
            container = client.containers.get(name)
            container.start()
            st.success(f"✅ Container '{name}' started.")
        except Exception as e:
            st.error(str(e))

# Stop a container
elif action == "Stop Container":
    name = st.text_input("Enter container name to stop")
    if st.button("Stop"):
        try:
            container = client.containers.get(name)
            container.stop()
            st.success(f"🛑 Container '{name}' stopped.")
        except Exception as e:
            st.error(str(e))

# Remove a container
elif action == "Remove Container":
    name = st.text_input("Enter container name to remove")
    if st.button("Remove"):
        try:
            container = client.containers.get(name)
            container.remove(force=True)
            st.success(f"🗑️ Container '{name}' removed.")
        except Exception as e:
            st.error(str(e))

# Launch new container
elif action == "Launch New Container":
    image = st.text_input("Image name (e.g., ubuntu)")
    name = st.text_input("Container name")
    if st.button("Launch"):
        try:
            client.containers.run(image, name=name, detach=True, tty=True)
            st.success(f"🚀 Container '{name}' launched using image '{image}'.")
        except Exception as e:
            st.error(str(e))

# Pull Docker image
elif action == "Pull Docker Image":
    image = st.text_input("Image name to pull (e.g., nginx:latest)")
    if st.button("Pull"):
        try:
            img = client.images.pull(image)
            st.success(f"⬇️ Image '{image}' pulled successfully.")
            st.write(img.tags)
        except Exception as e:
            st.error(str(e))
