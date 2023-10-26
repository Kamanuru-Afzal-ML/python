pip install speedtest-cli
import speedtest

def calculate_network_speed():
    # Create a Speedtest client
    st = speedtest.Speedtest()

    # Get the best server to test against
    st.get_best_server()

    # Perform download and upload speed tests
    download_speed = st.download() / 1_000_000  # Convert from bits per second to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert from bits per second to Mbps

    return download_speed, upload_speed

if __name__ == "__main__":
    download_speed, upload_speed = calculate_network_speed()
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
