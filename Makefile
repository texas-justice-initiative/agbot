LAMBDA_DEPLOYMENT_PACKAGE="build/lambda.zip"
PYTHON_SOURCES="*.py scrapers/*.py"
TMP_DIRECTORY="build/tmp"

build: clean
	mkdir -p ${TMP_DIRECTORY}
	rsync -R "${PYTHON_SOURCES}" ${TMP_DIRECTORY}
	pip3 install -r requirements.txt -t ${TMP_DIRECTORY}
	zip -r ${LAMBDA_DEPLOYMENT_PACKAGE} ${TMP_DIRECTORY} -i '*.py' '*.pem'
	rm -r ${TMP_DIRECTORY}

clean:
	rm -f ${LAMBDA_DEPLOYMENT_PACKAGE}
