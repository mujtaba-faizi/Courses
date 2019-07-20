var check = false;
var points = [];
var vertices = [[-0.5, -0.5], [0.5, -0.5], [0.0, 0.5]];
var vertex_properties;
var rotation_angle = 0.0;

function main() {
    
    var canvas = document.getElementById('clickable_canvas');
    var gl = getWebGLContext(canvas);
    if(!gl){console.log('Failed to Get Context');}
    
    var program = initShaders(gl, "vertex-shader", "fragment-shader");
    gl.useProgram(program);
    gl.program = program;
    
    vertex_properties = gl.getAttribLocation(program, 'properties');
    gl.vertexAttrib3f(vertex_properties, 1.0, rotation_angle, 0.0);
    
    gl.clearColor(0.0, 0.0, 0.0, 1.0);
    gl.clear(gl.COLOR_BUFFER_BIT);
    
    // initialize vertices for the triangle
    recurse(vertices[0], vertices[1], vertices[2], 0);
    var shape = initVertices(program, gl);
    render(gl, shape);
    
    /////////////////////////////////////////////
    ////////////dat GUI Properties///////////////
    /////////////////////////////////////////////
    var properties = function() {                
        this.Angle = 0.0;
        this.NumberOfRecursions = 0.0;
        this.Twist = false;
    };
    
    var configuration = new properties();
    var gui = new dat.GUI();

    var rotation_controller = gui.add(configuration, 'Angle', -360.0, 360.0);
    var recursion_controller = gui.add(configuration, 'NumberOfRecursions', 0, 6, 1); // Min and max
    
    var tess_controller = gui.add(configuration, 'Twist').listen().onFinishChange(function(value) {
        check = value;
        var fl = check ? 0.0 : 1.0;
        gl.vertexAttrib3f(vertex_properties, fl, rotation_angle, 0.0);
        render(gl, initVertices(program, gl));
        });
    
    rotation_controller.onChange(function(value){
        var fl = check ? 0.0 : 1.0;
        rotation_angle = value*Math.PI/180;
        gl.vertexAttrib3f(vertex_properties, fl, rotation_angle, 0.0);
        render(gl, initVertices(program, gl));
        });
    
    recursion_controller.onFinishChange(function(value){
        while(points.pop());
        var fl = check ? 0.0 : 1.0;
        gl.vertexAttrib3f(vertex_properties, fl, rotation_angle, 0.0);
        recurse(vertices[0], vertices[1], vertices[2], Math.ceil(value));
        render(gl, initVertices(program, gl));
    });
}

// renders a triangle
function render(gl, shape){
    gl.clearColor(0.0, 0.0, 0.0, 1.0);
    gl.clear(gl.COLOR_BUFFER_BIT);    
    gl.drawArrays(gl.TRIANGLES, 0, shape);
} 

// vertices for triangle
function initVertices(program, gl)
{
    var noOfDim = 2;
    var numberOfVertices = points.length;
    
    var vertexBuffer = gl.createBuffer();
    if(!vertexBuffer) { console.log('Failed to create the buffer object'); return -1;}
    
    gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, flatten(points), gl.STATIC_DRAW);
    
    var a_Position = gl.getAttribLocation(program, 'a_Position');
    if (a_Position < 0) { console.log("Failed to Get Position"); return;}
    
    gl.vertexAttribPointer(a_Position, noOfDim, gl.FLOAT, false, 0, 0);
    gl.enableVertexAttribArray(a_Position);
    
    return numberOfVertices;
}

// recurse until base count
function recurse(a, b, c, count) {
    if ( count == 0 ) {
        triangle(a, b, c);
    }
    else {
        var ab = centre(a, b, 0.5);
        var bc = centre(b, c, 0.5);
        var ca = centre(c, a, 0.5);
        recurse(a, ab, ca, count - 1);
        recurse(ab, bc, ca, count - 1);
        recurse(ab, b, bc, count - 1);
        recurse(ca, bc, c, count - 1);
    }
}

// vertices for each sub-triangle
function triangle(a, b, c) {
    points.push(a);
    points.push(b);
    points.push(c);
}

// returns centre coordinates of a line
function centre(u, v, s)
{
    var result = [];
    for ( var i = 0; i < u.length; ++i ) {
        result.push( (1.0 - s) * u[i] + s * v[i] );
    }
    return result;
}
