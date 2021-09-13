cleanbuild: clean build

build:
	jb build .
	python scripts/post_build.py

.PHONY: clean
clean:
	jb clean .

deploydev:
	aws s3 sync _build/html s3://py5dev.ixora.io/
