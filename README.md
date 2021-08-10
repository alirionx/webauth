# webauth

A simple microservice for central Token-based authentication between web apps. 
<br>
Python Flask in the backend and VueJS as SPA in the Frontend.

  

**Build SPA (Web-Frontend) in Docker**

    $ chmod +x build-dist_in-docker.sh 
    $ ./build-dist_in-docker.sh
  
  <br>
  
**Build Docker Image and run Container (Example)**

    $ docker build -t webauth .
    $ docker run -itd -p 8080:80 --name mywebauth webauth:latest

Open your browser and navigate to:
http://YOURDOCKERHOST:8080/#/init