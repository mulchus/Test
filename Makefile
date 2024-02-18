help:
	@echo "Tasks in \033[1;32mdemo\033[0m:"
	@cat Makefile

exc:
	python3 -c "print('Start')"
	python3 some_exceptions.py

heart:
	python3 heart_turtle.py

about: about2   # run about2 first
	python3 -c "print('End about')"

about2:
	python3 -c "print('See Makefile in https://habr.com/ru/companies/piter/articles/700282')"

calc:
	python3 -c "print(int(input('a = ')) + int(input('b = ')))"

# make -n about - Don't actually run any recipe; just print them.
# make -s about - Don't echo recipes.
