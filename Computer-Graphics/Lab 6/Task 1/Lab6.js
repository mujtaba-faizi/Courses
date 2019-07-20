window.onload = function() {


	
	var canvas = document.getElementById('webgl');
	var gl = getWebGLContext(canvas);
	if(!gl){
		console.log('Failed to find context');
	}

	var program = initShaders(gl, "vertex-shader", "fragment-shader");
	gl.useProgram(program);
	gl.program = program;

	var vertices=[-0.1,-0.1,0.1,-0.1,0,0.1,-0.25,0.25,-0.25,-0.25,0.25,0.25,0.25,-0.25,-0.4,0.0,0.4,0.0,0.0,0.4,0.0,-0.4]; 
var numberOfVertices=initVertices(program,gl,vertices);

	render(gl,numberOfVertices);


}

function animate(currentangle,time,elapsed){
	time=Date.now();
	elapsed=time-timePrev;
	timePrev=time;
	return (currentangle+(elapsed/1000));
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
return numberOfVertices;


}


function render(gl, numberOfVertices){
	gl.clearColor(0.0, 0.0, 0.0, 1.0);
	gl.clear(gl.COLOR_BUFFER_BIT);

	mat4.identity(mvMatrix);
	mat4.translate(mvMatrix,mvMatrix,[-0.5,0.3,0.0]);
	mat4.rotateZ(mvMatrix,mvMatrix,-1.5708);
	initTransformations(gl,mvMatrix);
	gl.drawArrays(gl.TRIANGLES, 0, 3);

	mat4.identity(mvMatrix);
	mat4.translate(mvMatrix,mvMatrix,[-0.5,0.0,0.0]);
	mat4.rotateZ(mvMatrix,mvMatrix,-1.5708);
	initTransformations(gl,mvMatrix);
	gl.drawArrays(gl.TRIANGLES, 0, 3);

	mat4.identity(mvMatrix);
	mat4.translate(mvMatrix,mvMatrix,[-0.5,-0.3,0.0]);
	mat4.rotateZ(mvMatrix,mvMatrix,-1.5708);
	initTransformations(gl,mvMatrix);
	gl.drawArrays(gl.TRIANGLES, 0, 3);

	mat4.identity(mvMatrix);
	mat4.translate(mvMatrix,mvMatrix,[0.5,0.3,0.0]);
	mat4.rotateZ(mvMatrix,mvMatrix,1.5708);
	initTransformations(gl,mvMatrix);
	gl.drawArrays(gl.TRIANGLES, 0, 3);

	mat4.identity(mvMatrix);
	mat4.translate(mvMatrix,mvMatrix,[0.5,0.0,0.0]);
	mat4.rotateZ(mvMatrix,mvMatrix,1.5708);
	initTransformations(gl,mvMatrix);
	gl.drawArrays(gl.TRIANGLES, 0, 3);

	mat4.identity(mvMatrix);
	mat4.translate(mvMatrix,mvMatrix,[0.5,-0.3,0.0]);
	mat4.rotateZ(mvMatrix,mvMatrix,1.5708);
	initTransformations(gl,mvMatrix);
	gl.drawArrays(gl.TRIANGLES, 0, 3);

	mat4.identity(mvMatrix);
	mat4.translate(mvMatrix,mvMatrix,[0.0,0.5,0.0]);
	mat4.rotateZ(mvMatrix,mvMatrix,3.14159);
	initTransformations(gl,mvMatrix);
	gl.drawArrays(gl.TRIANGLES, 0, 3);

	mat4.identity(mvMatrix);
	mat4.translate(mvMatrix,mvMatrix,[0.0,-0.5,0.0]);
	mat4.rotateZ(mvMatrix,mvMatrix,0.0);
	initTransformations(gl,mvMatrix);
	gl.drawArrays(gl.TRIANGLES, 0, 3);

	mat4.identity(mvMatrix);
	initTransformations(gl,mvMatrix);
	gl.drawArrays(gl.TRIANGLE_STRIP, 3, 4);

	mat4.identity(mvMatrix);
	initTransformations(gl,mvMatrix);
	gl.drawArrays(gl.LINES, 7, 2);

	mat4.identity(mvMatrix);
	initTransformations(gl,mvMatrix);
	gl.drawArrays(gl.LINES, 9, 2);
}