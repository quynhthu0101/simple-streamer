import threading
import cv2
import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.set_page_config(page_title='Webcam streamer', layout='wide')

col1, col2 = st.columns(2)

lock = threading.Lock()
img_container = {"img": None}


def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    with lock:
        img_container["img"] = img
    return 

with col1: 
    ctx = webrtc_streamer(key="example", 
                          video_frame_callback=video_frame_callback,

                          var myPeerConnection = new RTCPeerConnection({
                              iceServers: [
                                  {
                                    urls: "stun:stun.relay.metered.ca:80",
                                  },
                                  {
                                    urls: "turn:global.relay.metered.ca:80",
                                    username: "23c878901a70d3424c5a535c",
                                    credential: "itC5WX5n319BH+BU",
                                  },
                                  {
                                    urls: "turn:global.relay.metered.ca:80?transport=tcp",
                                    username: "23c878901a70d3424c5a535c",
                                    credential: "itC5WX5n319BH+BU",
                                  },
                                  {
                                    urls: "turn:global.relay.metered.ca:443",
                                    username: "23c878901a70d3424c5a535c",
                                    credential: "itC5WX5n319BH+BU",
                                  },
                                  {
                                    urls: "turns:global.relay.metered.ca:443?transport=tcp",
                                    username: "23c878901a70d3424c5a535c",
                                    credential: "itC5WX5n319BH+BU",
                                  },
                              ],
                            });
             


imgout_place = col2.empty()

while ctx.state.playing:
    with lock:
        img = img_container["img"]
    if img is None:
        continue
    # Phát hiên khuôn mặt sẽ đặt ở đây
    # Kết quả trả về là imgout có đóng khung khuôn mặt
    imgout = cv2.flip(img, 0)

    imgout_place.image(imgout, channels='BGR')

