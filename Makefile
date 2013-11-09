#Makefile

EXECUTABLE := spellcheck

SOURCES := *.py

EXT := exe
CC := python

all:
	$(CC) $(SOURCES) -o $(EXECUTABLE).$(EXT)

realclean:
	find . -type f -name "*.o" -exec rm '{}' \;
	find . -type f -name "*.exe" -exec rm '{}' \;

# this line required by make - don't delete
