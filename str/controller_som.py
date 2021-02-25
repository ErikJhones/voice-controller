import pyautogui
import time
import winsound

#****************************************************************
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

#***************************************************************
def controlar(comando, lado1):
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 500  # Set Duration To 1000 ms == 1 second
    

    distancia = 1 #passo da Mae
    comando = comando #comando a seguir
    lado = lado1

    if len(comando.split(' ')) > 1:
        distancia_texto, comando = comando.split(' ')
        
        if type(textoToNum(distancia_texto)) == int:
            print(distancia_texto)
            distancia = textoToNum(distancia_texto)
    

    if comando in ['cima']:
        pyautogui.press('space') 
        
    elif comando in ['apertar', 'pressione', 'pressionar']:
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

    elif comando in ['falem', 'fábio', 'falo', 'fale', 'vale', 'prole', 'sorri']:
        pyautogui.press('f')
        
    elif comando == 'baixo':
        x=1
        
    elif comando in ['esquerda', 'esquerdo']:
        lado = comando
        pyautogui.keyUp('right')

        start = time.time()
        while time.time() - start < 0.25*distancia: #0.25 é um passo da mae
            pyautogui.keyDown('left')
        pyautogui.keyUp('left')
        
    elif comando in ['direita', 'direito']:
        lado = comando
        pyautogui.keyUp('left')

        start = time.time()
        while time.time() - start < 0.25*distancia: #0.25 é um passo da mae
            pyautogui.keyDown('right')
        pyautogui.keyUp('right')
        
    elif comando in ['corra', 'correr']:
        x=1
        
    elif comando in ['virar', 'vire', 'virem', 'vir']:
        if lado in ['esquerda','esquerdo']:
            lado = 'direita'
            pyautogui.press('right')
        else:
            lado = 'esquerda'
            pyautogui.press('left')
        
    elif comando in ['onde', 'ande']:
        if lado in ['esquerda','esquerdo']:
            pyautogui.keyDown('left')
        else:
            pyautogui.keyDown('right')

    elif comando in ['pare']:
        pyautogui.keyUp('right')
        pyautogui.keyUp('left')
    
    elif comando in ['longo']:
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

    winsound.Beep(frequency, duration)
    return lado