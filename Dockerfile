FROM node:12.16.2-alpine3.11

RUN apk update && apk upgrade && \
    apk add --no-cache git 

USER node
WORKDIR /home/node
RUN git clone https://github.com/hakimel/reveal.js.git
WORKDIR /home/node/reveal.js
RUN npm install

RUN mkdir -p /home/node/reveal.js/slides

ADD ./menu.html index.html

CMD npm start