%{
	#include<stdio.h>
	#include<stdlib.h>
	extern int yylex();
%}

%union {
	int f;
}

%token <f> NUM
%type <f> E F T

%% 
S : E		{printf("%d \n", $1); }
  ;
E : E '+' F 	{$$ = $1 + $3;}
  | F			{$$ = $1; }
  ;
F : F '*' T	{$$ = $1 * $3; }
  | NUM	{$$ = $1;}
  ;
T : NUM {$$ = $1;}
  ;
%%

int main()
{
	yyparse();
	return 0;
}

