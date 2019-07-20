%{
#include<stdio.h>
#define stack_size 25
static int s_ptr, stack [stack_size];

static void push(int input){
	
	if(++s_ptr<stack_size){
		printf("\n%d",input);
		stack[s_ptr]=input;}
	else
		printf("\nstack is full!\n");
}

static int pop(){
	if(s_ptr>=0){ 
		printf("\n%d",stack[s_ptr]);
		return stack[s_ptr--];
	}
}
%}

%%
[0-9]+          {push (atoi(yytext));}
"+"             {printf ("\n\n+"); push (pop() + pop()); }
"*"             {printf ("\n\n*");  push (pop() * pop());}
"-"             {printf ("\n\n-"); int rhs= pop(); push (pop() - rhs);}
"/"             {printf ("\n\n/"); int rhs= pop(); push (pop() / rhs);}
;                        {printf ("\n%d\n", pop());}
[ \t\n]                  ;
%%


int yywrap()
{
return 1;
}

int main()
{
	printf("Postfix + - * / implemented!\n");
	s_ptr=-1;
	yylex();
	return 0;
}
