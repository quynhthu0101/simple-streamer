import threading
import cv2
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase, RTCConfiguration

# Cấu hình STUN/TURN servers
RTC_CONFIGURATION = RTCConfiguration(
    {
        "iceServers": [
            {"urls": "stun:stun.relay.metered.ca:80"},
            {
                "urls": "turn:global.relay.metered.ca:80",
                "username": "23c878901a70d3424c5a535c",
                "credential": "itC5WX5n319BH+BU",
            },
            {
                "urls": "turn:global.relay.metered.ca:80?transport=tcp",
                "username": "23c878901a70d3424c5a535c",
                "credential": "itC5WX5n319BH+BU",
            },
            {
                "urls": "turn:global.relay.metered.ca:443",
                "username": "23c878901a70d3424c5a535c",
                "credential": "itC5WX5n319BH+BU",
            },
            {
                "urls": "turns:global.relay.metered.ca:443?transport=tcp",
                "username": "23c878901a70d3424c5a535c",
                "credential": "itC5WX5n319BH+BU",
            },
        ]
    }
)

# Setup giao diện Streamlit
st.set_page_config(page_title='Webcam streamer', layout='wide')
col1, col2 = st.columns(2)

lock = threading.Lock()
img_container = {"img": None}

# Hàm xử lý khung hình video
def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    with lock:
        img_container["img"] = img
    return frame  # Bạn cần trả về frame nếu không sử dụng VideoTransformer

# Cột hiển thị webcam
with col1:
    ctx = webrtc_streamer(
        key="example",
        video_frame_callback=video_frame_callback,
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={"video": True, "audio": False},
    )

# Cột hiển thị ảnh đã xử lý
imgout_place = col2.empty()

# Vòng lặp hiển thị ảnh đã xử lý
if ctx:
    while ctx.state.playing:
        with lock:
            img = img_container["img"]
        if img is None:
            continue
        imgout = cv2.flip(img, 0)  # Giả sử đây là xử lý ảnh
        imgout_place.image(imgout, channels='BGR')
