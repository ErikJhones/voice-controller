from vosk import Model, KaldiRecognizer
import os
import pyaudio
import json
import pyautogui
import time

import os

lado_atual = 'direita'

def textoToNum(distancia):
    if distancia == 'dois':
        return 2
    elif distancia == 'três':
        return 3
    elif distancia == 'quatro':
        return 4
    elif distancia == 'cinco':
        return 5
    elif distancia == 'seis':
        return 6
    elif distancia == 'sete':
        return 7

def controlar(comando, lado1):
    distancia = 1 #passo da Mae
    comando = comando #comando a seguir
    lado = lado1

    if len(comando.split(' ')) > 1:
        distancia_texto, comando = comando.split(' ')
        
        if type(textoToNum(distancia_texto)) == int:
            print(distancia_texto)
            distancia = textoToNum(distancia_texto)
    

    if comando == 'cima':
        pyautogui.press('space') 
        
    elif comando == 'apertar' or comando == 'pressione' or comando == 'pressionar':
        start = time.time()
        while time.time() - start < 0.25:
            pyautogui.keyDown('left')
            pyautogui.keyDown('space')
        pyautogui.keyUp('left')
        pyautogui.keyUp('space')
        
        
    elif comando in ['salte','saltar','soltos','saltos', 'solto']:
        if lado in ['esquerda','esquerdo']:
            start = time.time()
            while time.time() - start < 0.25:
                pyautogui.keyDown('left')
                pyautogui.keyDown('space')
            pyautogui.keyUp('left')
            pyautogui.keyUp('space')
        else:
            start = time.time()
            while time.time() - start < 0.25:
                pyautogui.keyDown('right')
                pyautogui.keyDown('space')
            pyautogui.keyUp('right')
            pyautogui.keyUp('space')

    elif comando in['falem', 'fábio', 'fábio', 'falo', 'fale', 'vale','prole','sorri']:
        pyautogui.press('f')
        
    elif comando == 'baixo':
        x=1
        
    elif comando == 'esquerda' or comando == 'esquerdo':
        lado = comando
        pyautogui.keyUp('right')

        start = time.time()
        while time.time() - start < 0.25*distancia: #0.25 é um passo da mae
            pyautogui.keyDown('left')
        pyautogui.keyUp('left')
        
    elif comando == 'direita' or comando == 'direito':
        lado = comando
        pyautogui.keyUp('left')

        start = time.time()
        while time.time() - start < 0.25*distancia: #0.25 é um passo da mae
            pyautogui.keyDown('right')
        pyautogui.keyUp('right')
        
        
    elif comando == 'corra' or comando == 'correr':
        x=1
        
    elif comando in ['virar', 'vire', 'virem', 'vir']:
        if lado in ['esquerda','esquerdo']:
            lado = 'direita'
            pyautogui.press('right')
        else:
            lado = 'esquerda'
            pyautogui.press('left')
    
    elif comando == 'copiar':
        pyautogui.hotkey('ctrl', 'c')
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' %( 0.1, 400))
        
    elif comando in ['onde', 'ande']:
        if lado in ['esquerda','esquerdo']:
            pyautogui.keyDown('left')
        else:
            pyautogui.keyDown('right')

    elif comando == 'pare':
        pyautogui.keyUp('right')
        pyautogui.keyUp('left')
    
    elif comando == 'longo':
        if lado in ['esquerda','esquerdo']:
            start = time.time()
            while time.time() - start < 0.5:
                pyautogui.keyDown('left')
                pyautogui.keyDown('space')
            pyautogui.keyUp('left')
            pyautogui.keyUp('space')
        else:
            start = time.time()
            while time.time() - start < 0.5:
                pyautogui.keyDown('right')
                pyautogui.keyDown('space')
            pyautogui.keyUp('right')
            pyautogui.keyUp('space')


    return lado


model = Model('model')
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
        lado_atual = controlar(d, lado_atual)
        
        if d in  ['encerrado', 'encerrar','encerra','sérra', 'serra']:
            break
        #if 
    #else:
    #print(rec.PartialResult())

print(rec.FinalResult())