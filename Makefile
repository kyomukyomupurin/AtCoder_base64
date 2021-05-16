CC = g++-10
CFLAGS = -std=c++20 -O2
PYTHON = python3.9
TARGET = main


build: $(TARGET).cc
	$(CC) $(CFLAGS) $(TARGET).cc -o $(TARGET)

bin:
	@make -s build
	@$(PYTHON) bin.py $(TARGET).cc
