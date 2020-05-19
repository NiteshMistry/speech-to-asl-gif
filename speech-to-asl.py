import azure
import azure.cognitiveservices.speech as speechsdk
import pandas as pd
import csv
import re

# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = "88614528607345c6831e2f2fe96cbd37", "eastus"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Creates a recognizer with the given settings
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

print("Say something...")


# Starts speech recognition, and returns after a single utterance is recognized. The end of a
# single utterance is determined by listening for silence at the end or until a maximum of 15
# seconds of audio is processed.  The task repipturns the recognition text as result. 
# Note: Since recognize_once() returns only a single utterance, it is suitable only for single
# shot recognition like command or query. 
# For long-running multi-utterance recognition, use start_continuous_recognition() instead.
result = speech_recognizer.recognize_once()

# Checks result.

if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result.text))
    gif_key = result.text
    print(gif_key)
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details   .error_details))

#my_dict= pd.read_csv('meatu.csv').to_dict()
#d.read_csv('pandas_tutorial_read.csv', delimiter=';'
#print(my_dict)

with open('meatu.csv', mode='r') as infile:
     reader = csv.reader(infile)
     mydict = {rows[0]:rows[1] for rows in reader}
#print(mydict)

gif_url =  mydict.get(gif_key)

#print(gif_url)
#f = open("gifurl.txt","w+")
#f.write(gif_url)


myfile = r"C:\Users\ASUS\Desktop\ASL\gif.html"

html = '''
<html><head><title>ASL GIF</title><meta http-equiv="refresh" content="5"></head><body><img src="{URL}" alt="Sorry, I didn't get it." width=250/></body></html>
'''
new_html=html.format(URL=gif_url)

with open(myfile, "r+") as f:
    data = f.read()
    f.seek(0)
    f.write(new_html)
    f.truncate()
