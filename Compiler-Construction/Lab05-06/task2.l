import java.io.*;
%%
%class task2
%public
%type void
%function getNextToken

%{ 
	public static int[] arr;

 public static void main(String[] args) {
	  arr = new int[4];
 		try {
			InputStream is = new FileInputStream("in.txt");
			task2 s = new task2(is);
			s.getNextToken();
		}
		catch (IOException e) { }
 }
 
 public static void push(int v){
	arr[3] = arr[2];
	arr[2] = arr[1];
	arr[1] = arr[0];
	arr[0] = v;
 }
 
 public static void add(){
	arr[0] = arr[0]+arr[1];
	arr[1] = arr[2];
	arr[2] = arr[3];
	arr[3] = 0;
 }
 
 public static void mul(){
	arr[0] = arr[0]*arr[1];
	arr[1] = arr[2];
	arr[2] = arr[3];
	arr[3] = 0;
 }
 
 public static void sub(){
	arr[0] = arr[1]-arr[0];
	arr[1] = arr[2];
	arr[2] = arr[3];
	arr[3] = 0;
 }
 
 public static void printStack(){
	 System.out.println(arr[0] + " " + arr[1] + " " + arr[2] + " " + arr[3]);
 }
 
 public static int res(){
	 return arr[0];
 }
%} 

DIGIT=[0-9]+
ADD=[+]
MUL = [*]
SUB = [-]
NEWLINE = [\n]
SPACE = [\ ]

%% 

{DIGIT}  {push(Integer.parseInt(yytext()));printStack();}
{ADD} { add(); printStack(); }
{MUL} { mul(); printStack(); }
{SUB} { sub(); printStack(); }  
{SPACE}      { }
{NEWLINE}    {System.out.println("Result: " + res());}
.            { }