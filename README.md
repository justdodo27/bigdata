# bigdata

to run 
```
mapred streaming -files mapper_final.py,reducer_final.py,combiner_final.py -input input/min1.csv -output output -mapper mapper_final.py -reducer reducer_final.py -combiner combiner_final.py
```

to save the results
```
hadoop fs -getmerge output results.csv
```
