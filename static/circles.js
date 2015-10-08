function searchSong() {

  var url = "/songsearch.json"

  $.get(url, function (data){

		console.log(data);

		$("#song-title").text("Song Title: " + data.song_name);
		$("#song-artist").text("Artist: " + data.artist);      
		$("#song-genre").text("Genre: " + data.genre);      
		$("#song-spotify").html('<a href="' + data.spotify + '">Play Song on Spotify</a>')     

		prettyCirclesTogether(data.lyrics);

		// copyCollisionDetection(data.lyrics);
  })
}

function makePrettyCircles(data) {

	var circleViz = d3plus.viz()
		.container("#d3-area")
		.data(data)
		.type("bubbles")
		.id("word")
		.depth(1)
		.size("count", function(d){ return d * 1})
		.draw()
	
}
	
// $("#test").on("click", searchSong);

// this is to run multiple times to load database
$("#test").on("click", function() { setInterval(searchSong, 3000)});

var number = 1;
function repeatFunction() {
	if (number <= 1500) {
		searchSong;
		number++;
	}
}


function prettyCirclesTogether(data){

	var margin = {top: 20, right: 20, bottom: 30, left: 40},
		width = 960 - margin.left - margin.right,
		height = 500 - margin.top - margin.bottom;

	var nodes = d3.range(data.length + 1),
		root = nodes[0],
		color = d3.scale.category20();

	root.radius = 0;
	root.fixed = true;

	var force = d3.layout.force()
		.gravity(0.05)
		.charge(function(d, i) { return i ? 0: -2000; })
		.nodes(nodes)
		.size([width, height]);

	force.start();

	var svg = d3.select("body").append("svg")
		.attr("width", width)
		.attr("height", height);

	svg.selectAll("circle")
		.data(data)
	  .enter().append("circle")
	  	.attr("r", function(d) { return d.count; })
	  	.style("fill", function(d, i) { return color(i); })
	  	.text(function(d) { return d.word; });

	force.on("tick", function(e) {
		var q = d3.geom.quadtree(nodes),
			i = 0,
			n = nodes.length;

		while (++i < n) q.visit(collide(nodes[i]));

		svg.selectAll("circle")
			.attr("cx", function (d) { return d.x; })
			.attr("cy", function (d) { return d.y; });
	});

	svg.on("mousemove", function() {
		var p1 = d3.mouse(this);
		root.px = p1[0];
		root.py = p1[1];
		force.resume();
	});

	function collide(node) {
		var r = data.count + 16,
			nx1 = node.x - r,
			nx2 = node.x + r,
			ny1 = node.y - r,
			ny2 = node.y + r;
		return function (quad, x1, y1, x2, y2) {
			if (quad.point && (quad.point !== node)) {
				var x = node.x - quad.point.x,
					y = node.y - quad.point.y,
					l = Math.sqrt(x * x + y * y),
					r = data.count + quad.point.radius;
				if (l < r) {
					l = (l - r) / l * .5;
					node.x -= x*= l;
					node.y -= y *= l;
					quad.point.x += x;
					quad.point.y += y;
				}
			}
			return x1 > nx2 || x2 < nx1 || y1 > ny2 || y2 < ny1;
		};
	}

}


function copyCollisionDetection(data) {
	debugger;
	
	var width = 960,
	    height = 500;

	var data = data.lyrics
	var	word = function(data){ for (i; i < data.length ; i++) {return data.word}; }
	var	count = function(data){ return d.count};

	console.log(word);

	var nodes = d3.range(data.length).map(counts),
	    root = nodes[0],
	    color = d3.scale.category10();

	root.radius = 0;
	root.fixed = true;

	var force = d3.layout.force()
	    .gravity(0.05)
	    .charge(function(d, i) { return i ? 0 : -2000; })
	    .nodes(nodes)
	    .size([width, height]);

	force.start();

	var svg = d3.select("body").append("svg")
	    .attr("width", width)
	    .attr("height", height);

	svg.selectAll("circle")
	    .data(nodes.slice(1))
	  .enter().append("circle")
	    .attr("r", function(d) { return d.radius; })
	    .style("fill", function(d, i) { return color(i % 3); });

	force.on("tick", function(e) {
	  var q = d3.geom.quadtree(nodes),
	      i = 0,
	      n = nodes.length;

	  while (++i < n) q.visit(collide(nodes[i]));

	  svg.selectAll("circle")
	      .attr("cx", function(d) { return d.x; })
	      .attr("cy", function(d) { return d.y; });
	});

	svg.on("mousemove", function() {
	  var p1 = d3.mouse(this);
	  root.px = p1[0];
	  root.py = p1[1];
	  force.resume();
	});

	function collide(node) {
	  var r = node.radius + 16,
	      nx1 = node.x - r,
	      nx2 = node.x + r,
	      ny1 = node.y - r,
	      ny2 = node.y + r;
	  return function(quad, x1, y1, x2, y2) {
	    if (quad.point && (quad.point !== node)) {
	      var x = node.x - quad.point.x,
	          y = node.y - quad.point.y,
	          l = Math.sqrt(x * x + y * y),
	          r = node.radius + quad.point.radius;
	      if (l < r) {
	        l = (l - r) / l * .5;
	        node.x -= x *= l;
	        node.y -= y *= l;
	        quad.point.x += x;
	        quad.point.y += y;
	      }
	    }
	    return x1 > nx2 || x2 < nx1 || y1 > ny2 || y2 < ny1;
	  };
	}
}



