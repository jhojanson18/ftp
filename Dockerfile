FROM ubuntu:18.04
RUN apt update && apt install -y vsftpd && apt install -y ftp && apt install -y nano
RUN useradd -d /home/jhojan -m -s /bin/bash jhojan
RUN echo "jhojan:1234" | chpasswd
RUN mkdir  -p /home/jhojan/prueba && touch  /home/jhojan/prueba/prueba.txt
RUN mkdir -p /var/run/vsftpd/empty
EXPOSE 20 21 22
CMD ["/usr/sbin/vsftpd"]
