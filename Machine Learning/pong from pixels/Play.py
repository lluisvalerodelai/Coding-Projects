import numpy as np
import keyboard
import pyautogui
import time
from PIL import Image
from flattenimage import flattenImage





def captureScreen(elapsed_time):
    
    startime = time.time()
    
    images = []
    presses = []
    
    index = 0
    

    while (time.time() - startime) < elapsed_time:
        
        print(time.time())
        
        if keyboard.is_pressed('w'):
        
            screen = pyautogui.screenshot(region = (0, 38, 1280, 720))
            
            screen = screen.resize((int(1280/10), int(720/10)))
            
            screen.save(r'C:\Users\35840\Desktop\Luis Code\train\image' + str(index) + '.png')
            
            screen = np.array(screen)
            
            images.append(screen)
            presses.append(1)
        elif keyboard.is_pressed('s'):
            screen = pyautogui.screenshot(region = (0, 38, 1280, 720))
            
            screen = screen.resize((int(1280/10), int(720/10)))
            
            screen.save(r'C:\Users\35840\Desktop\Luis Code\train\image' + str(index) + '.png')
            
            screen = np.array(screen)
            
            images.append(screen)
            presses.append(0)
            
            
        
        if keyboard.is_pressed('q'):
            break
    
   
        index += 1

    images = np.array(images)
    
    return images, np.array(presses)





time.sleep(3)

images, presses = captureScreen(300)

images = flattenImage(images)

np.save(r'C:\Users\35840\Desktop\Luis Code\train\imgs.npy', images)
np.save(r'C:\Users\35840\Desktop\Luis Code\train\presses.npy', presses)


print(images.shape)
print(presses.shape)
