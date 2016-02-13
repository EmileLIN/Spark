from pyspark import SparkConf,SparkContext

conf = SparkConf().setMaster("local").setAppName("My App")
sc = SparkContext(conf=conf)

#RDDs Tranformation
lines=sc.textFile("/home/emilelin/Documents/Spark/Chapter3/textfile3-1")
filter_line = lines.filter(lambda s:"s" in s)

#RDDs Action
for line in filter_line.take(5):
	print line 




