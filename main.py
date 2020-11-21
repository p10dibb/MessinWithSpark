import pyspark
sc = pyspark.SparkContext("test").appName("cpts415-bigdata")


  
txt = sc.textFile('file:////usr/share/doc/python/copyright')
print(txt.count())

python_lines = txt.filter(lambda line: 'python' in line.lower())
print(python_lines.count())