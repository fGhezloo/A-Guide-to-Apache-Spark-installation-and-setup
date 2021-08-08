from pyspark import SparkConf, SparkContext
conf = SparkConf().setAppName("PySpark App").setMaster("spark://master:7077")
sc= SparkContext("local", "PySpark App")
confusedRDD = sc.textFile("test.txt")
coll=confusedRDD.take(5)
print("Elements in RDD -> %s" % (coll))

mappedconfusion = confusedRDD.map(lambda line : line.split(" "))

coll=mappedconfusion.take(5)

print("Elements in RDD -> %s" % (coll))


flatMappedConfusion = confusedRDD.flatMap(lambda line : line.split(" "))
coll=flatMappedConfusion.take(5)
print("Elements in RDD -> %s" % (coll))

onlyconfusion = confusedRDD.filter(lambda line : ("confus" in line.lower()))
coll=onlyconfusion.count()
print("Elements in RDD -> %i" % (coll))

coll=onlyconfusion.collect()
print("Elements in RDD -> %s" % (coll))
