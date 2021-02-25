from vosk import Model, KaldiRecognizer
import os
import pyaudio
import json

import controller_som

lado_atual = 'direita'

model = Model('..\model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()
a = ''

print('******************INICIO**********************\n')
while True:
    data = stream.read(8000) #4000
    '''if len(data) == 0:
        break'''
    if rec.AcceptWaveform(data):
        #a = rec.Result()
        d = json.loads(rec.Result())['text']
        #d['text']
        print(d)
        if len(d) > 0:
            lado_atual = controller_som.controlar(d, lado_atual)
        
        if d in  ['encerrado', 'encerrar','encerra','sérra', 'serra']:
            break

print(rec.FinalResult())