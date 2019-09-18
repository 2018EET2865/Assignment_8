all: ps1 ps2
ps1:
	lex ps1.l
	gcc -o ps1.out lex.yy.c
	./ps1.out ps1.txt
ps2:
	# yacc ps2.y
	lex ps2.l
	# cc lex.yy.c y.tab.c -o ps2.out
	gcc -o ps2.out lex.yy.c
	./ps2.out ps2.txt output.txt
# test2:
# 	lex test2.l
# 	yacc test2.y
# 	cc lex.yy.c test2.tab.c -o test2.out
# 	./test2.out 
 
clean:
	rm *.out