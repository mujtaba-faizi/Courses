var FizzyText = function() {

  this.angle = 0.0;
  // Define render logic ...

};

window.onload = function() {


  var text = new FizzyText();
  var gui = new dat.GUI();
  var angle_controller = gui.add(text, 'angle', 0.0, 360.0);

	
	var canvas = document.getElementById('webgl');
	var gl = getWebGLContext(canvas);
	if(!gl){
		console.log('Failed to find context');
	}

	var program = initShaders(gl, "vertex-shader", "fragment-shader");
	gl.useProgram(program);
	gl.program = program;

	var vertices=[-0.7,0.7, -0.5, 0.3, -0.3, 0.7,0,0.3,0.3,0.9]; 
	var numberOfVertices = initVertices(program,gl,vertices);
	tr=[0.5,0.5,0];
	angle=0;
	initTrans(gl,tr);
	initRot(gl,angle);
	render(gl, numberOfVertices);

	var vertices=[-0.7,0, -0.5, -0.4, -0.3, 0,0,-0.4,0.3,0.2,0.3,-0.2]; 
	var numberOfVertices = initVertices(program,gl,vertices);
	tr=[-0.5,-0.5,0];
	angle=0;
	initTrans(gl,tr);
	initRot(gl,angle);
		gl.drawArrays(gl.TRIANGLE_STRIP, 0, numberOfVertices);

	angle_controller.onChange(function(value) {
 	var vertices=[-0.7,0.7, -0.5, 0.3, -0.3, 0.7,0,0.3,0.3,0.9]; 
	var numberOfVertices = initVertices(program,gl,vertices);
	tr=[0.5,0.5,0];
	initTrans(gl,tr);
	initRot(gl,value);
	render(gl, numberOfVertices);

	var vertices=[-0.7,0, -0.5, -0.4, -0.3, 0,0,-0.4,0.3,0.2,0.3,-0.2]; 
	var numberOfVertices = initVertices(program,gl,vertices);
	tr=[-0.5,-0.5,0];
	angle=0;
	initTrans(gl,tr);
	initRot(gl,value);
		gl.drawArrays(gl.TRIANGLE_STRIP, 0, numberOfVertices);
	});

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


function initTrans(gl,tr){

var trMatrix = [1.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,1.0,0.0,tr[0],tr[1],tr[2],1.0];
var transformationMatrix=gl.getUniformLocation(gl.program,'transformationMatrix');
gl.uniformMatrix4fv(transformationMatrix,false,flatten(trMatrix));


}

function initRot(gl,angle){
var rad=Math.PI*angle/180.0;
var cosB=Math.cos(rad);
var sinB=Math.sin(rad);
var trMatrix = [cosB,sinB,0.0,0.0,-sinB,cosB,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,1.0];
var transformationMatrix=gl.getUniformLocation(gl.program,'transformationMatrix');
gl.uniformMatrix4fv(transformationMatrix,false,flatten(trMatrix));


}

function render(gl, numberOfVertices){
	gl.clearColor(0.0, 0.0, 0.0, 1.0);
	gl.clear(gl.COLOR_BUFFER_BIT);
	gl.drawArrays(gl.TRIANGLE_STRIP, 0, numberOfVertices);
}