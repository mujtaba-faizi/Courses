function main(){
	
	var canvas = document.getElementById('webgl');
	var gl = getWebGLContext(canvas);
	if(!gl){
		console.log('Failed to find context');
	}

	var program = initShaders(gl, "vertex-shader", "fragment-shader");
	gl.useProgram(program);
	gl.program = program;

var shape=1;
var vertices=[-0.2,0.2, -0.7, 0.2, -0.45, 0.7];   // 1st triangle
var numberOfVertices=Triangle(program,gl,vertices);
render(gl, numberOfVertices);
gl.drawArrays(gl.TRIANGLES, 0, numberOfVertices);

vertices1=translate(vertices,0.9,0);   // 2nd triangle
vertices1=rotation(vertices1,0.785398);   // angle in radians
var numberOfVertices=Triangle(program,gl,vertices1);
gl.drawArrays(gl.TRIANGLES, 0, numberOfVertices);

vertices2=translate(vertices,0.9,-0.6);   // 3rd triangle
vertices2=rotation(vertices2,-0.785398);   // angle in radians
vertices2=scale(vertices2,2,2);
vertices2=translate(vertices2,0.2,0.7);
var numberOfVertices=Triangle(program,gl,vertices2);
gl.drawArrays(gl.TRIANGLES, 0, numberOfVertices);

vertices3=translate(vertices,0,-0.6);    // 4th triangle
vertices3=scale(vertices3,0.5,0.75);
vertices3=translate(vertices3,-0.2,-0.2);
var numberOfVertices=Triangle(program,gl,vertices3);
gl.drawArrays(gl.TRIANGLES, 0, numberOfVertices);
}



function Triangle(program, gl, vertices){


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
    
}