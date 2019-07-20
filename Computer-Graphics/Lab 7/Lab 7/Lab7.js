window.onload = function() {


	
	var canvas = document.getElementById('webgl');
	var gl = getWebGLContext(canvas);
	if(!gl){
		console.log('Failed to find context');
	}

	var program = initShaders(gl, "vertex-shader", "fragment-shader");
	gl.useProgram(program);
	gl.program = program;

colors=[1.0,0.0,0.0,1.0,0.0,1.0,0.0,1.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0,0.0];
	var vertices=[-0.7,-0.5, 0.5, -0.5, -0.7, 0.5,0.5, 0.5];
var numberOfVertices=initVertices(program,gl,vertices);

	render(gl,numberOfVertices);

  var red, green, blue;

var red = bilinear_interpolation(1.0,0.0,0.0,1.0,vertices[0],vertices[6],vertices[1],vertices[7],-0.7,0.1);
var green = bilinear_interpolation(0.0,0.0,1.0,1.0,vertices[0],vertices[6],vertices[1],vertices[7],-0.7,0.1);
var blue = bilinear_interpolation(0.0,1.0,0.0,1.0,vertices[0],vertices[6],vertices[1],vertices[7],-0.7,0.1);
console.log(red,green,blue);

}

function bilinear_interpolation(q11, q12, q21, q22, x1, x2, y1, y2, x, y)
{
    var x2x1, y2y1, x2x, y2y, yy1, xx1;
    x2x1 = x2 - x1;
    y2y1 = y2 - y1;
    x2x = x2 - x;
    y2y = y2 - y;
    yy1 = y - y1;
    xx1 = x - x1;
    return 1.0 / (x2x1 * y2y1) * ( (q11 * x2x * y2y) + (q21 * xx1 * y2y) + (q12 * x2x * yy1) + (q22 * xx1 * yy1) );
}


function initTransformations(gl,modelMatrix){
	var transformationMatrix=gl.getUniformLocation(gl.program,'transformationMatrix');
	gl.uniformMatrix4fv(transformationMatrix,false,flatten(modelMatrix));
}

function initVertices(program, gl, vertices){


var noOfDim=2;
var numberOfVertices=vertices.length/noOfDim;
var vertexBuffer=gl.createBuffer();
if(!vertexBuffer){
	console.log('Failed to create the buffer object');
	return -1;
}
gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
gl.bufferData(gl.ARRAY_BUFFER, flatten(vertices),gl.STATIC_DRAW);
var a_Position=gl.getAttribLocation(program,'a_Position');
if(a_Position<0){
	console.log("Failed to get position");
	return;
}
gl.vertexAttribPointer(a_Position, noOfDim, gl.FLOAT, false, 0,0);
gl.enableVertexAttribArray(a_Position);

colors=[1.0,0.0,0.0,1.0,0.0,1.0,0.0,1.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0,0.0];
var colorBuffer=gl.createBuffer();
gl.bindBuffer(gl.ARRAY_BUFFER, colorBuffer);
gl.bufferData(gl.ARRAY_BUFFER, flatten(colors),gl.STATIC_DRAW);
var a_color=gl.getAttribLocation(program,'a_color');
gl.vertexAttribPointer(a_color, 4, gl.FLOAT, false, 0,0);
gl.enableVertexAttribArray(a_color);

return numberOfVertices;


}


function render(gl, numberOfVertices){
	gl.clearColor(0.0, 0.0, 0.0, 1.0);
	gl.clear(gl.COLOR_BUFFER_BIT);

	mat4.identity(mvMatrix);
	initTransformations(gl,mvMatrix);
	gl.drawArrays(gl.TRIANGLE_STRIP, 0, numberOfVertices);
}