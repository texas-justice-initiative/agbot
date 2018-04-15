LAMBDA_DEPLOYMENT_PACKAGE=build/lambda.zip

build: clean
	mkdir -p build
	zip ${LAMBDA_DEPLOYMENT_PACKAGE} *.py scrapers/*.py

clean:
	rm -f ${LAMBDA_DEPLOYMENT_PACKAGE}
