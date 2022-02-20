build:
	python -m build

upload:
	python -m twine upload --repository testpypi dist/*

clean:
	git clean -Xdf
