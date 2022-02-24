build:
	python -m build

upload_test:
	python -m twine upload --repository testpypi dist/*

upload:
	python -m twine upload --repository pypi dist/*

clean:
	git clean -Xdf
