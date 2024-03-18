#############
# setup #
#############

docker_build: ## build docker image
	docker build -t streamlit .
.PHONY: docker_build


docker_run: ## run docker image
	 docker run -p 8080:8080 streamlit
.PHONY: docker_run
