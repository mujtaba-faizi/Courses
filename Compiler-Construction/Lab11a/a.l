%option noyywrap
%{
	#include<stdio.h>
	#include<stdlib.h>
	#include "ta.tab.h"
%}

%%

[0-9]+          {yylval.f=atoi(yytext); return NUM;}
"+"             {printf ("\n\n+"); return yytext[0];}
"*"             {printf ("\n\n*"); return yytext[0];}
[\t\n\f]		{;}
%%

