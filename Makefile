.DEFAULT_GOAL := build

LAMBDA_DEPLOYMENT_PACKAGE="build/lambda.zip"
PYTHON_SOURCES="*.py scrapers/*.py"
TMP_DIRECTORY="build/tmp"

build: clean
	mkdir -p ${TMP_DIRECTORY}
	rsync -R "${PYTHON_SOURCES}" ${TMP_DIRECTORY}
	pip3 install -r requirements.txt -t ${TMP_DIRECTORY}
	cd ${TMP_DIRECTORY} && zip -r tmp.zip . -i '*.py' '*.pem'
	mv ${TMP_DIRECTORY}/tmp.zip ${LAMBDA_DEPLOYMENT_PACKAGE}
	rm -r ${TMP_DIRECTORY}

clean:
	rm -f ${LAMBDA_DEPLOYMENT_PACKAGE}
