import numpy as np

def flattenImage(images):
    
    f_images = []

    for img in range(len(images)):
        
        print(f'processing image {img}')
        
        image = np.array([])
        
        for row in range(len(images[img])):
            
            for pixl in range(len(images[img][row])):
                avg = np.mean(images[img][row][pixl])
                
                image = np.append(image, avg)
                
        f_images.append(image)

    f_images = np.array(f_images)
    
    return f_images