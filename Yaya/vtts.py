import websocket
import json
import hashlib
import base64

# Constants
PLUGIN_NAME = "SpeakingYaYa"
PLUGIN_DEVELOPER = "YaYa"
AUTHENTICATION_TOKEN = None  # Will store the token after the first step

def send_request(ws, payload):
    """Helper function to send a request and receive a response."""
    ws.send(json.dumps(payload))
    response = ws.recv()
    return json.loads(response)

def authenticate_vts(ws):
    """Authenticate with VTube Studio."""
    global AUTHENTICATION_TOKEN

    # Step 1: Request an Authentication Token
    token_request = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": "1.0",
        "requestID": "TokenRequest",
        "messageType": "AuthenticationTokenRequest",
        "data": {
            "pluginName": PLUGIN_NAME,
            "pluginDeveloper": PLUGIN_DEVELOPER
        }
    }
    token_response = send_request(ws, token_request)
    if token_response["messageType"] == "AuthenticationTokenResponse":
        AUTHENTICATION_TOKEN = token_response["data"]["authenticationToken"]
        print("Received Authentication Token:", AUTHENTICATION_TOKEN)
    else:
        raise Exception("Failed to get authentication token.")

    # Step 2: Authenticate the Session
    secret = "MySecret"  # Replace with your own secret string
    auth_string = f"{PLUGIN_NAME}{PLUGIN_DEVELOPER}{AUTHENTICATION_TOKEN}{secret}"
    auth_hash = hashlib.sha256(auth_string.encode()).hexdigest()

    auth_request = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": "1.0",
        "requestID": "AuthRequest",
        "messageType": "AuthenticationRequest",
        "data": {
            "pluginName": PLUGIN_NAME,
            "pluginDeveloper": PLUGIN_DEVELOPER,
            "authenticationToken": AUTHENTICATION_TOKEN,
            "authenticationHash": auth_hash
        }
    }
    auth_response = send_request(ws, auth_request)
    if auth_response["messageType"] == "AuthenticationResponse":
        print("Authentication successful!")
    else:
        raise Exception("Authentication failed.")

def send_text_to_vts(ws, text):
    """Send text to VTube Studio for TTS."""
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": "1.0",
        "requestID": "TTSRequest",
        "messageType": "TextToSpeechRequest",
        "data": {
            "text": text
        }
    }
    response = send_request(ws, payload)
    return response

# Main Script
if __name__ == "__main__":
    # Create a WebSocket connection to VTube Studio
    ws = websocket.create_connection("ws://localhost:8001")

    try:
        # Authenticate with VTube Studio
        authenticate_vts(ws)

        # Read the text file
        with open("transcription.txt", "r", encoding="utf-8") as file:
            text = file.read()

        # Send text to VTube Studio
        response = send_text_to_vts(ws, text)
        print(f"Response from VTube Studio: {response}")
    finally:
        # Close the WebSocket connection
        ws.close()