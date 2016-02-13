from pyspark import SparkConf,SparkContext

conf = SparkConf().setMaster("local").setAppName("My App")
sc = SparkContext(conf=conf)

if sc != None:
	print "sucess"
else:
	print "not success"
