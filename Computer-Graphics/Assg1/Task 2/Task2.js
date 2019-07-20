var FizzyText = function() {

  this.tesellation = 0;
  this.angle = 0.0;
  // Define render logic ...

};



window.onload = function() {
	
tesselation=0;

var	vertices=[-0.5,-0.5,0.5,-0.5,0,0.5]

  var text = new FizzyText();
  var gui = new dat.GUI();
  var tesellation_controller =  gui.add(text, 'tesellation', 0, 5).step(1);
  var angle_controller = gui.add(text, 'angle', 0.0, 360.0);

  	var canvas = document.getElementById('webgl');
	var gl = getWebGLContext(canvas);
	if(!gl){
		console.log('Failed to find context');
	}


	var program = initShaders(gl, "vertex-shader", "fragment-shader");
	gl.useProgram(program);
	gl.program = program;

	var a_Position = gl.getAttribLocation(program, 'a_Position');
	if(a_Position < 0){
		console.log("Failed to Get Position");
		return;
	}

		
		render1(gl);
  render(gl,vertices,0);

angle_controller.onChange(function(value) {
	value=Math.PI*value/180.0;
 	vertices1=rotation(vertices,value);
 	render1(gl);
	render(gl,vertices1,tesselation);
	
});

tesellation_controller.onChange(function(value) {
	tesselation=value;
	render1(gl);
  render(gl,vertices,value);
});


 	

	

};


function draw(program, gl, vertices){


var len = vertices.length;
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
var u_FragColor=gl.getUniformLocation(program,'u_FragColor');
if(u_FragColor<0){
	console.log("Failed to get color");
	return;
}
gl.uniform4f(u_FragColor,Math.random(),Math.random(),Math.random(),1.0);
return numberOfVertices;
}

function distance(x1,y1,x2,y2){
	return Math.sqrt(((y2-y1)*(y2-y1))+((x2-x1)*(x2-x1)));
}

function render1(gl){
	gl.clearColor(0.0, 0.0, 0.0, 1.0);
	gl.clear(gl.COLOR_BUFFER_BIT);
}

function render(gl,vertices, no){
	console.log(no);
		if (no<1){

draw(gl.program,gl,vertices);
gl.drawArrays(gl.TRIANGLES, 0, 3); 
return 0;
}

else{
	console.log("inside render")
	dist1=(distance(vertices[0],vertices[1],vertices[2],vertices[3]))/2;
	console.log("vertices1",dist1);
	dist2=(distance(vertices[0],vertices[1],vertices[4],vertices[5]))/2;
	dist3=(distance(vertices[2],vertices[3],vertices[4],vertices[5]))/2;
	dist4=(distance(vertices[4],vertices[5],vertices[2],vertices[5]))/2;
	vertices1=[vertices[0],vertices[1],dist1+vertices[0],vertices[1],(dist1/2)+vertices[0],dist2+vertices[1]];
	vertices2=[dist1+vertices[0],vertices[1],vertices[2],vertices[3],(dist1/2)+dist1+vertices[0],dist2+vertices[1]];
	vertices3=[(dist1/2)+vertices[0],dist2+vertices[1],(dist1/2)+dist1+vertices[0],dist2+vertices[1],dist1+vertices[0],vertices[1]];
	vertices4=[(dist1/2)+vertices[0],dist2+vertices[1],(dist1/2)+dist1+vertices[0],dist2+vertices[1],vertices[4],vertices[5]];

		render(gl,vertices1,no-1);
		render(gl,vertices2,no-1);
		render(gl,vertices3,no-1);
		render(gl,vertices4,no-1);

	return 1;
}
}
