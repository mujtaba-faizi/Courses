
function create(a, dim){

var arrayLength = 3;	 // set array length
var multiArray = new Array(arrayLength);

if (dim==3){    // for 3x3 matrix

for (var i = 0; i < multiArray.length; i++) {
  multiArray[i] = new Array(arrayLength);
}

// add items to first array index
multiArray[0][0] = a[0];
multiArray[0][1] = a[1];
multiArray[0][2] = a[2];

// second
multiArray[1][0] = a[3];
multiArray[1][1] = a[4];
multiArray[1][2] = a[5];

// third
multiArray[2][0] = a[6];
multiArray[2][1] = a[7];
multiArray[2][2] = a[8];

}

else{   // for 3x1 matrix

multiArray[0] = a[0];
multiArray[1] = a[1];
multiArray[2] = a[2];

 }

return multiArray;

}


function mult(a,b){

	var arrayLength = 3;	
var result = new Array(arrayLength);

for (var i = 0; i < result.length; i++) {
  result[i] = (a[i][0]*b[0])+(a[i][1]*b[1])+(a[i][2]*b[2]);
}

return result;

}

function dist(x,y){
	return Math.sqrt((x*x)+(y*y));
}

function twist(vertices,angle){

X1=(vertices[0]*Math.cos(angle*dist(vertices[0],vertices[1])))-(vertices[1]*Math.sin(angle*dist(vertices[0],vertices[1])));
Y1=(vertices[0]*Math.sin(angle*dist(vertices[0],vertices[1])))+(vertices[1]*Math.cos(angle*dist(vertices[0],vertices[1])));
X2=(vertices[2]*Math.cos(angle*dist(vertices[2],vertices[3])))-(vertices[3]*Math.sin(angle*dist(vertices[2],vertices[3])));
Y2=(vertices[2]*Math.sin(angle*dist(vertices[2],vertices[3])))+(vertices[3]*Math.cos(angle*dist(vertices[2],vertices[3])));
X3=(vertices[4]*Math.cos(angle*dist(vertices[4],vertices[5])))-(vertices[5]*Math.sin(angle*dist(vertices[4],vertices[5])));
Y3=(vertices[4]*Math.sin(angle*dist(vertices[4],vertices[5])))+(vertices[5]*Math.cos(angle*dist(vertices[4],vertices[5])));
vertices=[X1,Y1,X2,Y2,X3,Y3];   // updated coordinates
return vertices;

}

function rotation(vertices,angle){

var rot=[Math.cos(angle), -Math.sin(angle), 0, Math.sin(angle), Math.cos(angle),0,0,0,1];
rot=create(rot,3);
A=[vertices[0],vertices[1],1];
A=create(A, 1);
B=[vertices[2],vertices[3],1];
B=create(B, 1);
C=[vertices[4],vertices[5],1];
C=create(C, 1);
result=mult(rot, A);
X1=result[0];
Y1=result[1];
result=mult(rot, B);
X2=result[0];
Y2=result[1];
result=mult(rot, C);
X3=result[0];
Y3=result[1];
vertices=[X1,Y1,X2,Y2,X3,Y3];   // updated coordinates
return vertices;

}

function scale(vertices,x,y){
	var sc=[x, 0, 0, 0, y,0,0,0,1];
sc=create(sc,3);
A=[vertices[0],vertices[1],1];
A=create(A, 1);
B=[vertices[2],vertices[3],1];
B=create(B, 1);
C=[vertices[4],vertices[5],1];
C=create(C, 1);
result=mult(sc, A);
X1=result[0];
Y1=result[1];
result=mult(sc, B);
X2=result[0];
Y2=result[1];
result=mult(sc, C);
X3=result[0];
Y3=result[1];
vertices=[X1,Y1,X2,Y2,X3,Y3];   // updated coordinates
return vertices;
}

function translate(vertices,x,y){
	var sc=[1, 0, x, 0, 1,y,0,0,1];
sc=create(sc,3);
A=[vertices[0],vertices[1],1];
A=create(A, 1);
B=[vertices[2],vertices[3],1];
B=create(B, 1);
C=[vertices[4],vertices[5],1];
C=create(C, 1);
result=mult(sc, A);
X1=result[0];
Y1=result[1];
result=mult(sc, B);
X2=result[0];
Y2=result[1];
result=mult(sc, C);
X3=result[0];
Y3=result[1];
vertices=[X1,Y1,X2,Y2,X3,Y3];   // updated coordinates
return vertices;
}