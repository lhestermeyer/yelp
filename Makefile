build: 
	docker build -t docker_builds/notebook -f Dockerfile.notebook .

download:
	@echo "Please download the data from Yelp dataset"

run:
	docker run -p 8888:8888 docker_builds/notebook

build-server: 
	docker build -t docker_builds/server -f Dockerfile.server ./endpoint

run-server:
	docker run -p 8000:8000 docker_builds/server

presentation:
	jupyter nbconvert notebooks/20_RestaurantRatingChanges.ipynb --to slides --no-prompt --TagRemovePreprocessor.remove_input_tags={\"remove-input\"} --post serve --SlidesExporter.reveal_theme=simple