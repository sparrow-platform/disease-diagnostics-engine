Dockerhub link - https://hub.docker.com/r/jaylohokare/diseases-predictor

<h1>Installation:</h1>

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

````
