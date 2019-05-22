Installation:

System requiremenst - 
1. Python3.x
2. 16GB disk 


<b>Quick setup</b>
Enter docker folder and run
```
docker-compose up
```

The API will be live at 192.168.99.100:5000


<b>To build dockerfile from scratch :</b>
1. Download database umls.db from - 
https://drive.google.com/file/d/1BmnzCv2hjU49vXxBv_kI4FUae-lIAdz0/view?usp=sharing

2. Download 'data' folder from - 
https://drive.google.com/file/d/1nwD3aEMwW5CF8CWOscOT3IMztuNBpaYq/view?usp=sharing

3. Place 'data' folder and umls.b in docker folder of the repo<br>
4. The docker file currently downloads code from github repo. Change docker file if you want to build local code.<br>
Enter the docker folder and run
Docker build command - 
```
docker build -m 25g -t medicalapi .
```

To deploy after building - 
```
docker run -d -p 5000:5000 medicalapi
```

