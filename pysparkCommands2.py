from pyspark import SparkContext
sc = SparkContext("local", "count app")
words = sc.parallelize (
   ["scala",
   "java",
   "hadoop",
   "spark",
   "akka",
   "spark vs hadoop",
   "pyspark",
   "pyspark and spark"]
)
# counts = words.count()
coll = words.collect()
print("Elements in RDD -> %s" % (coll))
# print("Number of elements in RDD -> %i" % (counts))

# def f(x): print(x)
# fore = words.foreach(f)
#
words_filter = words.filter(lambda x: 'spark' in x)
filtered = words_filter.collect()
print("Fitered RDD -> %s" % (filtered))
#
# words_map = words.map(lambda x: (x, 1))
# mapping = words_map.collect()
# print("Key value pair -> %s" % (mapping))
#
#
# from operator import add
# nums = sc.parallelize([1, 2, 3, 4, 5])
# adding = nums.reduce(add)
# print("Adding all the elements -> %i" % (adding))
