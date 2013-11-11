#Makefile

EXECUTABLE := spellcheck

SOURCES := *.py

EXT := py
CC := python

py:
	$(CC) $(SOURCES) $(EXECUTABLE).$(EXT) $(ARG)

realclean:
	find . -type f -name "*.o" -exec rm '{}' \;
	find . -type f -name "*.exe" -exec rm '{}' \;

# this line required by make - don't delete
