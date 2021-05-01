#!/bin/bash

proj_name="get_url_data"

dev_container="${proj_name}_dev"
prod_container="${proj_name}_prod"

dev_build="${proj_name}:dev"
prod_build="${proj_name}:prod"
	
	
case $1 in
	"build")
		docker build -t ${dev_build} -f Dockerfile_dev .
		;;
	"run")
		docker run --rm -ti --name ${dev_container} -v $(pwd):/home/jovyan/work -p 8888:8888 ${dev_build}
		;;
	"build-prod")
		docker build -t ${prod_build} -f Dockerfile .
		;;
	"run-prod")
		#docker run --rm -ti --name ${prod_container} -v $(pwd)/app:/app -p 8081:80 ${prod_build}
		docker run --rm -ti --name ${prod_container} -p 8081:80 ${prod_build}
		;;	
	*)
		echo "dev_container -> ${dev_container}"
		;;
esac
