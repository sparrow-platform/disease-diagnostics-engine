<h1>About</h1>
This is an API to serve disease diagnostics based on UMLS databases. Disease diagnostics engine is a part of Sparrow AI.
The API has endpoints to:

```
1. Get disease names (with probabilities) given symptoms
2. Suggest symptoms (correct names, related symptoms)
3. Get information on diseases, medicines
```

This repo acts as core part of SparrowAI. The API is triggered by IBM Watson Assistant via Sparrow middleware.

<p align="center">
<img  max-height=500 src="https://sparrow-platform.com/images/sparrow/MedicalInfoEngine.png"/>
</p>

<h1>Technical details</h1>
This project is a FLASK based API interfacing database (Currently SQLite).
Due to large size of the database, we have not hosted the database on cloud, but have created the API in a way that changing sqlite.py in umls folder to custom database connector will easily help us migrate the project to cloud based database like IBM DB2. 

<p align="center">
<img  max-height=400 src="https://raw.githubusercontent.com/sparrow-platform/disease-diagnostics-engine/master/DiseaseDiagnosticEngine.png"/>
</p> 

<h1>Installation:</h1>
Dockerhub link - https://hub.docker.com/r/jaylohokare/diseases-predictor

<b>Quick setup</b><br>

```
docker-compose up
```
The API will be live at 192.168.99.100:5000 (Windows) 127.0.0.1:5000 (Linux/Mac)


<b>To build using dockerfile:</b><br>

1. Download database umls.db and place it in umls/databases - 
https://drive.google.com/file/d/1BmnzCv2hjU49vXxBv_kI4FUae-lIAdz0/view?usp=sharing

2. Download 'data' folder and place it at root location - 
https://drive.google.com/file/d/1nwD3aEMwW5CF8CWOscOT3IMztuNBpaYq/view?usp=sharing

3. Docker build command - 
```
docker build -m 25g -t medicalapi .
```

To run after building - 
```
docker run -d -p 5000:5000 medicalapi
```

Other docker useful commands-
```
#Clear all docker images cache
docker system prune -a

#Get all docker instances
docker container ls


#To push to docker hub
docker images 
docker tag ID jaylohokare/diseases-predictor:0.3
docker push jaylohokare/diseases-predictor
````
