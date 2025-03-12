from stt import recognize_speech
from llm_module import generate_response
#from tts_module import generate_speech
#from vtube_module import send_parameter_to_vts
#from lip_sync_module import send_phoneme_data
from expression_module import analyze_sentiment, trigger_expression

def process_input(user_input):
    # Generate response from Deepseek R1
    print("inside main.py")
    response = generate_response("transcription.txt")
    print(response)
    
    #Analyze sentiment and trigger expression
    expression = analyze_sentiment(response)
    print(expression)
    #trigger_expression(expression)
    
    # Generate speech
    #generate_speech(response, "response.wav")
    
    # Run lip-syncing
    #send_phoneme_data("phonemes.json")

if __name__ == "__main__":
    # Example user input
    file = recognize_speech()
    process_input(file)