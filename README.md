# bigdata

to run 
```
mapred streaming -D stream.num.map.output.key.fields=4 -files mapper_final.py,reducer_final.py,combiner_final.py -input input/input.csv -output output -mapper mapper_final.py -reducer reducer_final.py -combiner combiner_final.py
```

to save the results
```
hadoop fs -getmerge output results.csv
```


run pig *oink oink*
```
pig -x tez -f nyc.pig -param input_dir3=input -param input_dir4=input  -param output_dir6=output
```
