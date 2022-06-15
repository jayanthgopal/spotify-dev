import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "1f87728885ec42db8e6e2bc953c8f702"
CLIENT_SECRET = "6303b01284414894acd0dff37f3ed3a5"

st.set_page_config(page_title="Spotify Weekly",layout="wide")
st.title("Spotify Weekly")

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())