In order for this system to run the following libraries are required:
   
    -Sklearn
    -Pandas
    -Numpy
    -NLTK
    -elasticsearch
    -langdetect
    

Recommend pip installing them 

constant.py should be checked before trying to run anything
in here all paths and index names used are stored, please change any relevant fields!

Firstly run datacleaning.py will create a new dataset in Datasets folder
then run indexing.py which will index this dataset into elasticsearch
finally run reindex.py which will apply all preprocessing to the datastet and upload 
a new index to elastic search.


