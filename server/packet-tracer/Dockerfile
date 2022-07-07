FROM ubuntu:16.04
RUN apt-get update && apt-get install -y tar wget curl xauth libqt5webkit5 libqt5xml5 libqt5multimedia5 libqt5script5 libqt5scripttools5 \
 && mkdir -p /home/pt  
WORKDIR /home/pt
COPY . .

 
ENV HOME /home/pt

#ENV DISPLAY=host.docker.internal:0.0 
ENV DISPLAY=:0
CMD /home/pt/bin/PacketTracer7
