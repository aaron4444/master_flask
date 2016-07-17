#
# Second Flask App Dockerfile
#
#

# Pull base image.
FROM centos:7.0.1406

# Build commands
RUN yum install -y python-setuptools mysql-connector-python mysql-devel gcc python-devel git
RUN easy_install pip
RUN mkdir /opt/master_flask
WORKDIR /opt/master_flask
ADD requirements.txt /opt/master_flask
RUN pip install -r requirements.txt
ADD . /opt/master_flask

# Define working directory.
#WORKDIR /opt/master_flask

# Define default command.
# CMD ["python", "manage.py", "runserver"]
