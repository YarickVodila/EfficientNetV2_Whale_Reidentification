import os
import glob
import pandas as pd
import numpy as np
import cv2
data= np.array([])
data_test = np.array([])
train_dir = './train'
test_dir = './test'

def apply_mask(image, mask):
    return cv2.bitwise_and(image,image,mask = mask)

#print(len(glob.glob(os.path.join('.\\Whale ReId 2_mm\\'+path_number,path,'*.jpg'))))
count = 0
count_test = 0
for path_number in os.listdir('.\\Whale ReId 2_mm'):
    #print(path_number)
    for path in os.listdir('.\\Whale ReId 2_mm\\'+path_number):
        i = 0
        for img_jpg in glob.glob(os.path.join('.\\Whale ReId 2_mm\\'+path_number,path,'*.jpg')):
            print(i)
            if i < 17:
                i += 1
                file_name = os.path.basename(img_jpg) #название в jpg с расширением
                #print(file_name)
                file_jpg = os.path.splitext(img_jpg)[0] #название фото jpg без расширения и с путём

                image =cv2.imread(file_jpg+'.jpg')
                mask = cv2.imread(file_jpg+'.png', 0)
                #print(file_name)
                resultant = apply_mask(image, mask)
                #cv2.imwrite(os.path.join(train_dir,str(count)+'.jpg'), resultant) #сохраняем в папку с train

                data = np.append(data, np.array([str(count)+'.jpg', path_number])) #сохраняем в дату название и номер класса
                count += 1

            elif i >= 17 and i < 20:
                i += 1
                file_name = os.path.basename(img_jpg)  # название в jpg с расширением
                # print(file_name)
                file_jpg = os.path.splitext(img_jpg)[0]  # название фото jpg без расширения и с путём

                image = cv2.imread(file_jpg + '.jpg')
                mask = cv2.imread(file_jpg + '.png', 0)
                # print(file_name)
                resultant = apply_mask(image, mask)
                cv2.imwrite(os.path.join(test_dir, str(count_test) + 'qqq.jpg'), resultant)  # сохраняем в папку с train

                data_test = np.append(data_test, np.array([str(count_test) + '.jpg', path_number]))  # сохраняем в дату название и номер класса
                count_test += 1
            else:
                break

data = np.reshape(data,(int(data.shape[0]/2),2))
data_test = np.reshape(data_test,(int(data_test.shape[0]/2),2))
print(data_test)
        #print(path)
        #if path=='crop5_DJI_0130':
            #break
df = pd.DataFrame(data=data,columns=['ID_img', 'class'])
df_test = pd.DataFrame(data=data_test,columns=['ID_img', 'class'])
print(df.value_counts())
df.to_csv('train.csv', index= False)
df_test.to_csv('test.csv', index= False)