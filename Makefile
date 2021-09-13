cleanbuild: clean build

build:
	jb build .
	python scripts/post_build.py

.PHONY: clean
clean:
	jb clean .
