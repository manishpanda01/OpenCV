
# In[1]:
# Import modules
import cv2
import matplotlib.pyplot as plt
from dataPath import DATA_PATH


# In[2]:

import matplotlib
matplotlib.rcParams['figure.figsize'] = (10.0, 10.0)


# In[3]:


# Image Path
imgPath = DATA_PATH+"images/IDCard-Satya.png"

# Read image
img = cv2.imread(imgPath) 
# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#Display the image
plt.imshow(img_rgb)



# In[4]:


# Create a QRCodeDetector Object
# Variable name should be qrDecoder
qrDecoder = cv2.QRCodeDetector()

# Detect QR Code in the Image, Output should be stored in opencvData, bbox, rectifiedImage in the same order

opencvData,bbox,rectifiedImage = qrDecoder.detectAndDecode(img)
# print("Data:\n",opencvData)
# print("Rectified Image:\n",rectifiedImage)
# print("Bounding box:\n",bbox)
# Check if a QR Code has been detected
if opencvData != None:
    print("QR Code Detected")
else:
    print("QR Code NOT Detected")



# In[14]:


n = len(bbox)

# Draw the bounding box
for i in range(n):
    pt1 = tuple(bbox[i][0]) #Point1 
    pt2 = tuple(bbox[(i+1)%4][0]) #Point2
    cv2.line(img,pt1,pt2,(255,0,0),2) #Blue line
#Convert BGR to RGB
rgb_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(rgb_img)


# In[28]:


# Since we have already detected and decoded the QR Code
# using qrDecoder.detectAndDecode, we will directly
# use the decoded text we obtained at that step (opencvdata)

print("QR Code Detected!")
print("Decoded Text - ",opencvData)

# In[15]:


# Write the result image
resultImagePath = "QRCode-Output.png"
cv2.imwrite(resultImagePath,img)


# In[16]:


# Display the result image
plt.imshow(img)

# Notice anything wrong?


# In[17]:


# OpenCV uses BGR whereas Matplotlib uses RGB format
# So convert the BGR image to RGB image
# And display the correct image

rgb_image=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(rgb_image)






