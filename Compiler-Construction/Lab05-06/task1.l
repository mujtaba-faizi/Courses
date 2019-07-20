%{
#include<stdio.h>
%}
%%
"if"|"else"|"while"|"do"|"switch"|"case"|"begin"|"end"|"proedure"|"function" {ECHO; printf(" is Key Keyword\n");}
[a-zA-Z][a-z|0-9]* {ECHO; printf(" is Key Identifier\n");}
[0-9]* {ECHO; printf(" is Key Number\n");}
[+-]?([0-9]*[.])?[0-9]+ {ECHO; printf(" is Floating Point\n");}
"!"|"@"|"&"|"^"|"%"|"$"|"#" {ECHO; printf(" is Special Character\n");}
"+"|"-"|"*"|"/" {ECHO; printf(" is Arthmetic operator\n");}
%%
int yywrap()
{
return 1;
}
main()
{
printf("Enter a string of data\n");
yylex();
}




