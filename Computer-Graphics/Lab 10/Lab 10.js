var timePrev = Date.now();

var obj = {
  RotationSpeed: 1.0,
  Fovy: 1.0,
  Aspect: 1.0,
  Near: 1.0,
  Far: 10.0,
  a:0.0,
  b:0.0
};

function main() {
  var canvas = document.getElementById('webgl');
  var gl = getWebGLContext(canvas);
  if (!gl){
    console.log('Failed to find context');
  }

  var program = initShaders( gl, "vertex-shader", "fragment-shader" );
  gl.useProgram (program);
  gl.program = program;

  var numberOfVertices = initVertices(program, gl);

  gl.enable(gl.DEPTH_TEST);
  var vMatrix = mat4.create();
  var pMatrix = mat4.create();

  var currentangle = 0.0;
  var time, elapsed;
  var tick = function(){
    currentangle = animate(currentangle, time, elapsed);
    mat4.identity(vMatrix);
	mat4.lookAt(vMatrix, [0.0, 0.0, -1.0], [0.0, 0.0, -1.0], [0.0, 1.0, 0.0]);
	mat4.rotateY(vMatrix, vMatrix, obj.a);
    initProjection(gl, pMatrix);
    mat4.perspective(pMatrix, obj.Fovy, obj.Aspect, obj.Near, obj.Far);
     render(gl, numberOfVertices, vMatrix, currentangle);
    document.onkeydown = function(ev){ keyDownFunc(ev, gl, vMatrix, numberOfVertices, currentangle); };
   
    requestAnimationFrame(tick)
  }
  tick();
}

function initProjection(gl, pMatrix){
  var u_pMatrix = gl.getUniformLocation(gl.program, 'u_pMatrix');
  if (!u_pMatrix) {
      console.log('Failed to get the storage locations of proj');
      return;
    }
  gl.uniformMatrix4fv(u_pMatrix, false, flatten(pMatrix));
}

function initMVMatrix(gl, mvMatrix, vMatrix){
  mat4.multiply(mvMatrix, vMatrix, mvMatrix);
  var u_mvMatrix = gl.getUniformLocation(gl.program, 'u_mvMatrix');
  gl.uniformMatrix4fv(u_mvMatrix, false, flatten(mvMatrix));

}

function keyDownFunc(ev, gl, vMatrix, numberOfVertices,currentangle){
	console.log(ev.keyCode);

	if(ev.keyCode == 39) { // The right arrow key was pressed

		obj.a+=0.02;

	} else if (ev.keyCode == 37) { // The left arrow key was pressed
		
		obj.a-=0.02;
	}

	else if (ev.keyCode == 38) {
	
	if(obj.Fovy>0.0){
		obj.Fovy-=0.02;}

	} else if (ev.keyCode == 40) {

		if(obj.Fovy<3.0){
		obj.Fovy+=0.02;}
	}
}

function render (gl, numberOfVertices, vMatrix, angle){

  gl.clearColor(0.0, 0.0, 0.0, 1.0);
  gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

  mat4.identity(mvMatrix);
  mat4.translate(mvMatrix, mvMatrix, [0.5, -0.25, -3.0]);
  mat4.rotateX(mvMatrix, mvMatrix, angle);
  mat4.rotateY(mvMatrix, mvMatrix, angle);
  mat4.rotateZ(mvMatrix, mvMatrix, angle);
  initMVMatrix(gl, mvMatrix,  vMatrix);
  gl.drawArrays(gl.LINE_LOOP, 0, 17);

  mat4.identity(mvMatrix);
  mat4.translate(mvMatrix, mvMatrix, [-0.5, -0.2, -5.0]);
  mat4.rotateX(mvMatrix, mvMatrix, angle);
  mat4.rotateY(mvMatrix, mvMatrix, angle);
  mat4.rotateZ(mvMatrix, mvMatrix, angle);
  initMVMatrix(gl, mvMatrix,  vMatrix);
  gl.drawArrays(gl.LINE_LOOP, 17, 17);

  mat4.identity(mvMatrix);
    mat4.translate(mvMatrix, mvMatrix, [0.0, 0.3, -10.5]);
  initMVMatrix(gl, mvMatrix,  vMatrix);
  gl.drawArrays(gl.TRIANGLE_FAN, 34, 5);

}

function initVertices(program, gl){
  var vertices = [
            -0.25, -0.25, -0.25, 1.0, 0.0, 0.0, 1.0,      // Red
          0.25, -0.25, -0.25, 1.0, 0.0, 0.0, 1.0,
          0.25, 0.25, -0.25, 1.0, 0.0, 0.0, 1.0,
          -0.25, 0.25, -0.25, 1.0, 0.0, 0.0, 1.0,
          -0.25, -0.25, -0.25, 1.0, 0.0, 0.0, 1.0,

          -0.3, -0.3, 0.25, 1.0, 0.0, 0.0, 1.0,
          0.2, -0.3, 0.25, 1.0, 0.0, 0.0, 1.0,
          0.2, 0.2, 0.25, 1.0, 0.0, 0.0, 1.0,
          -0.3, 0.2, 0.25, 1.0, 0.0, 0.0, 1.0,
          -0.3, -0.3, 0.25, 1.0, 0.0, 0.0, 1.0,

          0.2, -0.3, 0.25, 1.0, 0.0, 0.0, 1.0,
          0.25, -0.25, -0.25, 1.0, 0.0, 0.0, 1.0,
          0.25, 0.25, -0.25, 1.0, 0.0, 0.0, 1.0,
          0.2, 0.2, 0.25, 1.0, 0.0, 0.0, 1.0,
          -0.3, 0.2, 0.25, 1.0, 0.0, 0.0, 1.0,
          -0.25, 0.25, -0.25, 1.0, 0.0, 0.0, 1.0,
          -0.25, -0.25, -0.25, 1.0, 0.0, 0.0, 1.0,

          -0.25, -0.25, -0.25, 0.0, 0.0, 1.0, 1.0,      // BLue
          0.25, -0.25, -0.25, 0.0, 0.0, 1.0, 1.0,
          0.25, 0.25, -0.25, 0.0, 0.0, 1.0, 1.0,
          -0.25, 0.25, -0.25, 0.0, 0.0, 1.0, 1.0,
          -0.25, -0.25, -0.25, 0.0, 0.0, 1.0, 1.0,

          -0.3, -0.3, 0.25, 0.0, 0.0, 1.0, 1.0,
          0.2, -0.3, 0.25, 0.0, 0.0, 1.0, 1.0,
          0.2, 0.2, 0.25, 0.0, 0.0, 1.0, 1.0,
          -0.3, 0.2, 0.25, 0.0, 0.0, 1.0, 1.0,
          -0.3, -0.3, 0.25, 0.0, 0.0, 1.0, 1.0,

          0.2, -0.3, 0.25, 0.0, 0.0, 1.0, 1.0,
          0.25, -0.25, -0.25, 0.0, 0.0, 1.0, 1.0,
          0.25, 0.25, -0.25, 0.0, 0.0, 1.0, 1.0,
          0.2, 0.2, 0.25, 0.0, 0.0, 1.0, 1.0,
          -0.3, 0.2, 0.25, 0.0, 0.0, 1.0, 1.0,
          -0.25, 0.25, -0.25, 0.0, 0.0, 1.0, 1.0,
          -0.25, -0.25, -0.25, 0.0, 0.0, 1.0, 1.0,

          -5.0,-1.0,10.0,0.0,1.0,0.0,1.0,
          5.0, -1.0,10.0,0.0,1.0,0.0,1.0,
          5.0, -1.0,-10.0,0.0,1.0,0.0,1.0,
          -5.0, -1.0,-10.0,0.0,1.0,0.0,1.0,
          -5.0,-1.0,10.0,0.0,1.0,0.0,1.0,
          ];

  vertices = flatten(vertices);
  var noOfDim = 3;
  var colorItemSize = 4;
  var numberOfVertices = vertices.length / (noOfDim + colorItemSize);
  var ELEMENT_SIZE = vertices.BYTES_PER_ELEMENT;  // array ( vertices) must be flatten or should be "FLOAT32ARAAY before call."
  

  var vertexBuffer = gl.createBuffer();
  if (!vertexBuffer){ console.log('Failed to create the buffer object '); return -1;}
  gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
  gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);

  var a_Position = gl.getAttribLocation(program, "a_Position");
  if (a_Position < 0) { console.log ("Failed to Get Position"); return; }
  gl.vertexAttribPointer(a_Position, noOfDim, gl.FLOAT, false, ELEMENT_SIZE*7, 0);
  gl.enableVertexAttribArray(a_Position);

  // setting up color
  var a_Color = gl.getAttribLocation(program, "a_Color");
  if (a_Color < 0) { console.log ("Failed to Get Color"); return; }

  gl.vertexAttribPointer(a_Color, colorItemSize, gl.FLOAT, false, ELEMENT_SIZE*7, ELEMENT_SIZE*3);
  gl.enableVertexAttribArray(a_Color);

  return numberOfVertices;
}

function animate(currentangle, time, elapsed){
  time = Date.now();
  elapsed = time - timePrev;
  timePrev = time;

  return (currentangle + (elapsed*obj.RotationSpeed / 1000));
}

