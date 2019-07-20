%{
	#include<stdio.h>
	#include<stdlib.h>
	extern int yylex();
%}

%union {
	int i;
	float f;
}

%token <i> INTT
%token <f> FOLL

%% 
S : E		{printf("%d \n", $1); }
  ;
E : F T 	{}
  ;
F : INTT	{}
  | FOLL	{}
  ;
T : id , T	{}
  | id
  ;
%%

int main()
{
	yyparse();
	return 0;
}

