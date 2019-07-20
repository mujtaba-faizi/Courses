import java.io.*;
%%
%class MyScanner
%public
%type int
%function getNextToken
%{ 
 public static void main(String[] args) {
 		try {
			InputStream is = new FileInputStream("input.txt");
			MyScanner s = new MyScanner(is);
			s.getNextToken();
		}
		catch (IOException e) { }
 }
%}

ALPHA=[A-Za-z]
DIGIT=[0-9]
SPACE=[\ ]
NEWLINE = [\n|\r|\r\n]
identifier = {ALPHA}({ALPHA})*
int_const = {DIGIT}+
MULTIPLY = [*]

%% 

{int_const}  { System.out.println("Integer Constant: "  + yytext());}  
{DIGIT}+{identifier} {System.out.println("Error: int literal followed by identifier: " + yytext());}
"write"        { System.out.println("Keyword: " + yytext()); }
{identifier} { System.out.println("Identifier: " + yytext()); }  
{SPACE}      { }
{NEWLINE}    { }
{MULTIPLY}         { System.out.println("Operator: MULTIPLY"); }
.            { System.out.println("Error: unrecognized symbol: "  + yytext()); }