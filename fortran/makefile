# makefile for the overlap programs
#   Shengquan Tuo  April 2010
#
# run make -f makefile overlap to create the overlap program.
CC = gcc
CFLAGS = -O  $(GRAPHINC)
NAGLIB = /psi/nagfl-18/lib/libnag.a /psi/NAGWare_f95-4.0/lib/libf95.a
overlap.o:		overlap.f
			g77 -O -c overlap.f

overlap:	overlap.o
		g77 -O overlap.o  -o overlap 
