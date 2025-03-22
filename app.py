import streamlit as st
from streamlit_mic_recorder import mic_recorder

# Initialize session state if it doesn't exist
if 'audio_output' not in st.session_state:
    st.session_state.audio_output = None

# Callback function to update session state
def callback():
    if st.session_state.my_recorder_output:
        st.session_state.audio_output = st.session_state.my_recorder_output['bytes']

# Button to start recording
audio = mic_recorder(
    start_prompt="Start Recording",
    stop_prompt="Stop Recording",
    key="my_recorder",
    format="webm",
    callback=callback
)

# Display the recorded audio after recording
if st.session_state.audio_output:
    st.audio(st.session_state.audio_output, format="audio/webm")
