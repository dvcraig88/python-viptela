mkdir sample
mkdir sample/templates
mkdir sample/static

cp sample-app.py sample/.
cp -r templates/* sample/templates/.
cp -r static/* sample/static/.

echo "FROM python" >> sample/Dockerfile
echo "RUN pip install flask" >> sample/Dockerfile
echo "COPY ./static /home/ubuntu/static/" >> sample/Dockerfile
echo "COPY ./templates /home/ubuntu/templates/" >> sample/Dockerfile
echo "COPY sample-app.py /home/ubuntu/" >> sample/Dockerfile
echo "EXPOSE 8080" >> sample/Dockerfile
echo "CMD python /home/ubuntu/sample-app.py" >> sample/Dockerfile

cd sample
sudo docker build -t sampleapp .

sudo docker stop samplerunning
sudo docker rm samplerunning
sudo docker run -t -d -p 8000:8080 --name samplerunning sampleapp
sudo docker ps -a
