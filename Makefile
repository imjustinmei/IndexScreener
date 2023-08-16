install:
	pip install -r requirements.txt

get:
	python src/getdata

process:
	python src/process

main:
	python src/getdata; \
	python src/process;