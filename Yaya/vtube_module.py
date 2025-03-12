import websocket
import json

# WebSocket URL for VTube Studio
VTS_WS_URL = "ws://localhost:8001"

# Function to send a parameter value to VTube Studio
def send_parameter_to_vts(parameter_name, value):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": "1.0",
        "requestID": "SomeID",
        "messageType": "InjectParameterDataRequest",
        "data": {
            "parameterValues": [
                {"id": parameter_name, "value": value}
            ]
        }
    }

    ws = websocket.create_connection(VTS_WS_URL)
    ws.send(json.dumps(payload))
    response = ws.recv()
    ws.close()
    print(f"Response from VTube Studio: {response}")