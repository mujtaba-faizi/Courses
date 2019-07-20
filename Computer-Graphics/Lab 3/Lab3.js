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
var numberOfVertices=Triangle(program,gl);
var noOfQuadVertices=Quad(program,gl);
		gl.clearColor(0.0, 0.0, 0.0, 1.0);
	gl.clear(gl.COLOR_BUFFER_BIT);
	// 1. Create the button
var triangle_button = document.createElement("button");
triangle_button.innerHTML = "Create a Triangle";

// 2. Append somewhere
var body = document.getElementsByTagName("body")[0];
body.appendChild(triangle_button);

// 3. Add event handler
triangle_button.addEventListener ("click", function() {
	shape=1;
  render(gl, numberOfVertices);
});
// 1. Create the button
var quad_button = document.createElement("button");
quad_button.innerHTML = "Create a Quad";

// 2. Append somewhere
var body = document.getElementsByTagName("body")[0];
body.appendChild(quad_button);

// 3. Add event handler
quad_button.addEventListener ("click", function() {
	shape=0;
   render(gl, noOfQuadVertices);
});
// 1. Create the button
var color_button = document.createElement("button");
color_button.innerHTML = "Change color";

// 2. Append somewhere
var body = document.getElementsByTagName("body")[0];
body.appendChild(color_button);

// 3. Add event handler
color_button.addEventListener ("click", function() {

   Color(program, gl,shape);
});
}

function Color(program, gl,shape){
	if (shape==1){
var noOfVertices=Triangle(program,gl);}
else{
var noOfVertices=Quad(program,gl);}
render(gl,noOfVertices);
var u_FragColor=gl.getUniformLocation(program,'u_FragColor');
if(u_FragColor<0){
	console.log("Failed to get color");
	return;
}
gl.uniform4f(u_FragColor,Math.random(),Math.random(),Math.random(),1.0);
}

function Triangle(program, gl){
var vertices=[-0.5,-0.5, 0.5, -0.5, 0, 0.5];
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

function Quad(program, gl){
var vertices=[0,-0.5, 0.5, -0.5, 0, 0.5,0.5, -0.5, 0.5, 0.5, 0,0.5];
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
    gl.drawArrays(gl.TRIANGLES, 0, numberOfVertices);
}