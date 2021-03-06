from pyspark import SparkConf,SparkContext

conf = SparkConf().setMaster("local").setAppName("My App")
sc = SparkContext(conf=conf)

#RDDs load data
lines=sc.textFile("/home/emilelin/Documents/Spark/Chapter3/textfile3-1")

#Map
map_words= lines.map(lambda line:line.split(" "))

#Action
print ("The map prints: \n")
for word in map_words.take(5):
	print word

print ("\n")
#Flat_Map
flatmap_words=lines.flatMap(lambda line:line.split(" "))

#Action 
print ("The flat map prints: \n")
for word in flatmap_words.take(10):
	print word

