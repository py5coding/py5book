cleanbuild: clean build

build:
	jb build .
	python scripts/post_build.py

	echo "Checking for core dumps (use make core_dumps to remove):"
	find . -name "*.log"
	echo "Build complete"

core_dumps:
	find . -name "*.log"
	find . -name "*.log" -exec rm {} \;

.PHONY: clean
clean:
	jb clean .
	find . -name "*.log" -exec rm {} \;

open:
	firefox _build/html/index.html &

deploydev:
	aws s3 sync --delete _build/html s3://dev.py5coding.org/

deployprod:
	aws s3 sync --delete _build/html s3://py5coding.org/
	aws configure set preview.cloudfront true
	aws cloudfront create-invalidation --distribution-id E3VCF8BC8C1QLY --paths '/*'
