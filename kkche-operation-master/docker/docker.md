
# curl -sSL https://get.docker.io/ubuntu/ | sudo sh
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9

sudo sh -c "echo deb https://get.docker.io/ubuntu docker main\
> /etc/apt/sources.list.d/docker.list"

sudo apt-get update

sudo apt-get install lxc-docker

sudo service docker start

sudo docker pull ubuntu:14.04
sudo docker search <image name>

sudo docker run ubuntu:14.04 /bin/echo 'Hello world'

sudo docker <command> --help
sudo docker

sudo docker run -t -i ubuntu:14.04 /bin/bash
sudo docker ps
sudo docker ps -l
sudo docker logs <id or names>
sudo docker logs -f <id or names>
sudo docker inspect <id or names>

sudo docker run -d -P training/webapp python app.py
sudo docker port <id or names> 5000

sudo docker stop <id or names>

sudo docker images

sudo docker run -d --name db training/postgres
sudo docker run -d -P --name web --link db:db training/webapp python app.py
sudo docker run -d -P --name web -v /webapp training/webapp python app.py
sudo docker run -d -P --name web -v /src/webapp:/opt/webapp training/webapp python app.py
sudo docker run -d -P --name web -v /src/webapp:/opt/webapp:ro training/webapp python app.py

# commit a image
sudo docker commit -m="bla..." -a="...." 0b2616b0e5a8 ouruser/sinatra:v2
# create a image
touch Dockerfile

```
FROM        ubuntu:14.04
RUN         apt-get update
RUN         apt-get -y install redis-server
EXPOSE      6379
ENTRYPOINT  ["/usr/bin/redis-server"]
```
# sudo docker build -t="<username>/<imagename>:<tag name>" <Dockerfile location>
sudo docker build -t="ouruser/sinatra:v2" .

sudo docker push ouruser/sinatra

# some images
crashsystems/gitlab-docker
pcting/hadoop-single-node
base/chef-server
okapies/chef-solo
