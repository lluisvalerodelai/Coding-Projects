import time
import numpy as np
from logisticregression import predict
import pyautogui
import keyboard
from flattenimage import flattenImage

X = np.load(r'C:\Users\35840\Desktop\Luis Code\train\imgs.npy')
y = np.load(r'C:\Users\35840\Desktop\Luis Code\train\presses.npy')


time.sleep(3)

index = 0

while True:
    screen = pyautogui.screenshot(region = (0, 38, 1280, 720))
                
    screen = screen.resize((int(1280/10), int(720/10)))
    
    screen = np.array(screen)
    
    image = np.array([])

    for row in range(len(screen)):
            
        for pixl in range(len(screen[row])):
            avg = np.mean(screen[row][pixl])
                
            image = np.append(image, avg)
    
    

    image = np.reshape(image, (-1, 1)).T
    
    prediction = predict(image)
    
    print(f'prediction {index} is: {prediction}')
    
    if prediction == 1:
        keyboard.press('w')
    else:
        keyboard.press('s')
        
    if keyboard.is_pressed('q'):
        break
    
    index += 1
    
    