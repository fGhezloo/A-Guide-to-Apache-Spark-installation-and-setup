from pyspark import SparkConf, SparkContext
import base64
import glob
import cv2
import numpy as np
from PIL import Image
import random

conf = SparkConf().setAppName("PySpark App").setMaster("spark://192.168.0.7:7077")
sc= SparkContext("local[2]", "PySpark App")



def grayscale(image_64_encode):
   directory="/home/ubuntu/Desktop/testout/"
   filename= directory  + str(random.randint(1,10000)) + ".jpg"
   image_64_decode=base64.b64decode(image_64_encode)
   image_result = open(filename, 'wb')  # create a writable image and write the decoding result
   image_result.write(image_64_decode)
   image = cv2.imread(filename)
   gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   # img = Image.open(filename).convert('L')
   # gray.save(filename)
   cv2.imwrite(filename, gray)
   return

file1 = open('/home/ubuntu/Desktop/testfile.txt', 'wb')
i=1
for filename in glob.glob('/home/ubuntu/Desktop/test/*'):
   image = open(filename, 'rb')
   image_read = image.read()
   image_64_encode = base64.b64encode(image_read)
   file1.write(image_64_encode)
   file1.write(b'\n')

file1.close()


RDD = sc.textFile("/home/ubuntu/Desktop/testfile.txt")
coll=RDD.count()
print("Elements in RDD -> %s" % (coll))
RDD.foreach(lambda x: grayscale(x))

