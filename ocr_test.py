from pyspark import SparkConf, SparkContext
import base64
import glob
import cv2
import numpy as np
import random
import codecs
import requests
import json
import platform

conf = SparkConf().setAppName("PySpark App").setMaster("spark://192.168.0.7:7077")
sc= SparkContext(conf=conf)

url1="http://172.17.0.2:9191/classify"
url2="http://172.17.0.4:9191/classify"

def main(image_64_encode):
    directory="/var2/input/images/"
    nontext="/var2/nontext/"
    text="/var2/text/"
    error="/var2/error/"
    random.randint(1,1000000)
    filename= str(random.randint(1,1000000))
    image_64_decode=base64.b64decode(image_64_encode)
    data = '{ "urls":[], "base64":["' + image_64_encode + '"]}'
    platformNum=platform.node()
    if platformNum[-1]== 1:
        response = requests.post(url1, data=data, headers={"Content-Type": "application/json"})
        print(platformNum)
        print(response)
    else:
        response = requests.post(url2, data=data, headers={"Content-Type": "application/json"})
        print(platformNum)
        print(response)
    try:
        out=response.json()
        if out['result'][0]['class'] == 'textful' :
            file2 = open( text + filename +'.txt', 'wb')
            file2.write((out['result'][0]['text']).encode('utf-8'))
            file2.close()
            image_result = open(text + filename + '.jpg', 'wb')
            image_result.write(image_64_decode)
            image_result.close()
        else:
            image_result = open(nontext + filename + '.jpg', 'wb')
            image_result.write(image_64_decode)
            image_result.close()
    except:
        image_result = open(error + filename + '.jpg', 'wb')
        image_result.write(image_64_decode)
        image_result.close()
    return

file1 = open('/var2/encodedimages.txt', 'wb')
i=1
for filename in glob.glob('/var2/test/*'):
    image = open(filename, 'rb')
    image_read = image.read()
    image_64_encode = base64.b64encode(image_read)
    file1.write(image_64_encode)
    file1.write(b'\n')
file1.close()


RDD = sc.textFile("/var2/encodedimages.txt")
coll=RDD.count()
print("Elements in RDD -> %s" % (coll))
RDD.foreach(lambda x: main(x))                                                                      
