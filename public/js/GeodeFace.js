		   // each point has [id, affinity, x, y, z]
GeodeFace = function(points) {

  THREE.Geometry.call(this);

  this.ids = [];
  this.affinities = [];
  for (i = 0; i < 3; i++) {
    var p = points[i];
    this.ids.push(p[0]);
    this.affinities.push(p[1]);
    this.vertices.push(new THREE.Vector3(p[2], p[3], p[4]));
  }

  this.faces.push(new THREE.Face3(0,1,2));
  this.faceVertexUvs[0].push([new THREE.UV(0,0),new THREE.UV(1,0),new THREE.UV(1,1) ]);

  this.faces.push(new THREE.Face3(2,1,0));
  this.faceVertexUvs[0].push([new THREE.UV(0,0),new THREE.UV(1,0),new THREE.UV(1,1) ]);

  this.computeCentroids();
  this.computeFaceNormals();
};

GeodeFace.prototype = new THREE.Geometry();
GeodeFace.prototype.constructor = GeodeFace;