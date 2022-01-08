# API with FastAPI framework
API processing signatures.tsv file (table with data), allowing to search & get data from the table<br>

<h2>Docker</h2>
Building the docker image:<br>
$ docker build -t image-name1 .<br>
Starting the docker container:<br>
$ docker run -p 8000:8000 --name container-name1 fastapi-image1<br> 

<h2>Run the solution</h2>
$ docker-compose up<br>

<h2>Check the solution & outcomes</h2>
Open http://0.0.0.0:8000/docs in a browser<br>
Press "GET" button<br>
Press "Try it out" button<br>
Paste to patient_id section: id from the first column in signatures.tsv file. Input examples to try: NSCLC1155 NSCLC825 NSCLC1425<br>
Press "Execute" button<br>

