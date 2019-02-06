CC = gcc
CFLAGS = -g -pedantic
SRCD = src
INCD = include
OBJD = obj
EXEC = sha256

OBJFILES = cnf.o karloff_zwick.o preprocess.o operations.o hash.o main.o
OBJS = $(OBJFILES:%.o=$(OBJD)/%.o)

default: init $(EXEC)

init:
	@mkdir -p obj

$(EXEC): $(OBJS)
	$(CC) -o $@ $^ $(CFLAGS)

$(OBJD)/%.o: $(SRCD)/%.c
	$(CC) -o $@ -c $< -ansi $(CFLAGS)

.PHONY: clean, mrproper

clean:
	@rm -f $(OBJD)/*.o

mrproper: clean
	@rm -f $(EXEC)
