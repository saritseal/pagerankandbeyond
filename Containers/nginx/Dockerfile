FROM nginx:alpine
#FROM nginx

RUN apk add --update \
	nginx \
	openrc \
	bash \
	curl

#RUN rc-update add nginx default

# Copy a configuration file from the current directory
COPY nginx.conf /etc/nginx/nginx.conf

# Expose ports
#EXPOSE 7777

RUN mkdir -p /run/nginx

# Set the default command to execute when creating a new container
#CMD [ "nginx", "-g", "daemon off;" ]
#ENTRYPOINT "/etc/init.d/nginx"

