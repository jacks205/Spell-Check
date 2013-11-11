#Makefile

EXECUTABLE := spellcheck

SOURCES := *.py

EXT := py
CC := python

0:
	$(CC) $(SOURCES) 
	$(CC) $(EXECUTABLE).$(EXT) 0

1:
	$(CC) $(SOURCES) 
	$(CC) $(EXECUTABLE).$(EXT) 1

realclean:
	find . -type f -name "*.o" -exec rm '{}' \;
	find . -type f -name "*.exe" -exec rm '{}' \;

# this line required by make - don't delete
