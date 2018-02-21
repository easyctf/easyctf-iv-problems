FROM ubuntu:16.04

# Install nodejs
RUN apt-get -y update
RUN apt-get -y install curl build-essential sudo
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get -y install nodejs

# Install pillow
RUN apt-get -y install python3 python3-pip && \
    pip3 install --upgrade pip && \
    pip3 install --upgrade pillow numpy

# Install nsjail
RUN apt-get -y install \
    autoconf bison flex gcc g++ git libprotobuf-dev libtool \
    make pkg-config protobuf-compiler
RUN git clone --depth=1 https://github.com/google/nsjail.git
WORKDIR /nsjail
RUN make && mv /nsjail/nsjail /bin && rm -rf -- /nsjail
WORKDIR /

# for debugging pls
RUN apt-get -y install vim wget rsyslog

# Clean up
RUN rm -rf /var/lib/apt/lists/*

# Copy source code
COPY src /app

# Change working directory
WORKDIR /app

# Install dependencies
RUN npm install

# Make readonly
RUN chmod -R a-w /app && \
    mkdir -p /app/uploads && \
    chmod -R a+w /app/uploads

# Expose API port to the outside
EXPOSE 80
ENV PORT 80

# Launch application
#CMD ["sh", "-c", "service rsyslog start ; npm start"]
CMD ["npm", "start"]
