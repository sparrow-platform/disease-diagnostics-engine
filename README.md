1. The project runs on Python3.x
2. Install all requirements (pip install -r requirements.txt)
3. Download Database from - https://drive.google.com/file/d/1BmnzCv2hjU49vXxBv_kI4FUae-lIAdz0/view?usp=sharing
4. Place the umls.db file in /umls/databases and /databases

System requiremenst - 
1. Python3.x
2. 16GB disk 

Database file can be downloaded from -
https://drive.google.com/file/d/1BmnzCv2hjU49vXxBv_kI4FUae-lIAdz0/view?usp=sharing

Docker build command - 
```
docker build -m 25g -t medicalapi .
```

The docker image is available on dockerhub at - 

To deploy the api - 
```
docker-compose up
```
