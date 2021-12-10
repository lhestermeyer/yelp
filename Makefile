build: 
	docker build -t docker_builds/notebook -f Dockerfile.notebook

download:
	@echo "Please download the data from Yelp dataset"

run:
	docker run -p 8888:8888 docker_builds/notebook
	