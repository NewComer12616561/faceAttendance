import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from PIL import Image

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "",
    'storageBucket': ""
})

# Function to convert images to 216x216 PNG format
def convert_image(image_path):
    with Image.open(image_path) as img:
        img = img.resize((216, 216))  # Resize to 216x216
        png_image_path = os.path.splitext(image_path)[0] + '.png'  # Change extension to .png
        img.save(png_image_path, 'PNG')  # Save as PNG
    return png_image_path

# Importing student images
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []

for path in pathList:
    # Convert image to 216x216 PNG format
    original_image_path = os.path.join(folderPath, path)
    converted_image_path = convert_image(original_image_path)

    # Read the converted image
    imgList.append(cv2.imread(converted_image_path))
    studentIds.append(os.path.splitext(path)[0])

    # Upload to Firebase Storage
    fileName = f'{folderPath}/{os.path.basename(converted_image_path)}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(converted_image_path)

print(studentIds)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")
