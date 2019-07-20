var FizzyText = function() {

  this.color0 = "#ffae23"; // CSS string 
  this.size = 10.0;
  // Define render logic ...

};

window.onload = function() {


  var text = new FizzyText();
  var gui = new dat.GUI();
  var color_controller =  gui.addColor(text, 'color0');
  var size_controller = gui.add(text, 'size', 5.0, 30.0);

  	var canvas = document.getElementById('webgl');
	var gl = getWebGLContext(canvas);
	if(!gl){
		console.log('Failed to find context');
	}
	var tapCoordinates = [];
	canvas.onmousedown = function(ev){click(ev, gl, canvas, a_Position, tapCoordinates,program);};
	var reset_button = document.createElement("button");
reset_button.innerHTML = "RESET";

// 2. Append somewhere
var body = document.getElementsByTagName("body")[0];
body.appendChild(reset_button);

// 3. Add event handler
reset_button.addEventListener ("click", function() {
	gl.clear(0.0, 0.0, 0.0, 1.0);
	gl.clear(gl.COLOR_BUFFER_BIT);
	var tapCoordinates = [];
	canvas.onmousedown = function(ev){click(ev, gl, canvas, a_Position, tapCoordinates,program);};
});

size_controller.onChange(function(value) {
 		if (tapCoordinates.length<3){
 				 		numberOfVertices=draw(program,gl,tapCoordinates);
	render(gl,numberOfVertices);
 	var a_PointSize=gl.getAttribLocation(program,'a_PointSize');
if(a_PointSize<0){
	console.log("Failed to get point size");
	return;
}
gl.vertexAttrib1f(a_PointSize,value);
console.log(value);
	}
});

color_controller.onChange(function(value) {
 		numberOfVertices=draw(program,gl,tapCoordinates);
	render(gl,numberOfVertices);
var rgb=hexToRgb(value);
 	var u_FragColor=gl.getUniformLocation(program,'u_FragColor');
if(u_FragColor<0){
	console.log("Failed to get color");
	return;
}

gl.uniform4f(u_FragColor,rgb[0],rgb[1],rgb[2],1.0);
  
});


	var program = initShaders(gl, "vertex-shader", "fragment-shader");
	gl.useProgram(program);
	gl.program = program;

	var a_Position = gl.getAttribLocation(program, 'a_Position');
	if(a_Position < 0){
		console.log("Failed to Get Position");
		return;
	}
	gl.clear(0.0, 0.0, 0.0, 1.0);
	gl.clear(gl.COLOR_BUFFER_BIT);

};

function hexToRgb(hex) {
        if( hex=="" ) hex="000000";
        	if( hex.charAt(0)=="#" ) hex=hex.substring(1,hex.length);
        	if( hex.length!=6 )
        		return [0,0,0];
        	r = hex.substring(0,2);
        	g = hex.substring(2,4);
        	b = hex.substring(4,6);
        	r = parseInt(r, 16);
        	g = parseInt(g, 16);
        	b = parseInt(b, 16);
        	r = (r - 0) / (255 - 0);  // to normalize b/w 0 & 1
        	g = (g - 0) / (255 - 0);
        	b = (b - 0) / (255 - 0);
        	return [r,g,b];
}

function click(ev, gl, canvas, a_Position, tapCoordinates, program){
	var x = ev.clientX; 
	var y = ev.clientY;
	var rect = ev.target.getBoundingClientRect();

	x = ((x - rect.left) - canvas.height/2)/(canvas.height/2);
	y = (canvas.width/2 - (y - rect.top))/(canvas.width/2);

	tapCoordinates.push(x);
	tapCoordinates.push(y);

	numberOfVertices=draw(program,gl,tapCoordinates);
	render(gl,numberOfVertices);
	
}


function draw(program, gl, tapCoordinates){

var len = tapCoordinates.length;
var noOfDim=2;
var numberOfVertices=tapCoordinates.length/noOfDim;
var vertexBuffer=gl.createBuffer();
if(!vertexBuffer){
	console.log('Failed to create the buffer object');
	return -1;
}
gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
gl.bufferData(gl.ARRAY_BUFFER, flatten(tapCoordinates),gl.STATIC_DRAW);
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
	if (numberOfVertices==1){
		gl.drawArrays(gl.Points, 0, 1);
	}
	else if (numberOfVertices==2){
		gl.drawArrays(gl.LINES, 0, 2);
	}
	else{
    gl.drawArrays(gl.TRIANGLE_STRIP, 0, numberOfVertices);
}}
