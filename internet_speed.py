import speedtest

st = speedtest.Speedtest()

print("Testing download speed...")
download = st.download() / 1_000_000  # in Mbps
print(f"Download Speed: {download:.2f} Mbps")

print("Testing upload speed...")
upload = st.upload() / 1_000_000  # in Mbps
print(f"Upload Speed: {upload:.2f} Mbps")

ping = st.results.ping
print(f"Ping: {ping:.2f} ms")
