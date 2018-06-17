all:
	docker build --tag randocat:1 .
	docker run -p 8080:8080 -it -v $$PWD:/app randocat:1 python randocat.py
