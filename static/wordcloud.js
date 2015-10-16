function searchSong() {

  var url = "/songsearch.json"

  $.get(url, function (data){

		console.log(data);

		$("#song-title").text("Song Title: " + data.song_name);
		$("#song-artist").text("Artist: " + data.artist);      
		$("#song-genre").text("Genre: " + data.genre);      
		$("#song-spotify").html('<a href="' + data.spotify + '">Play Song on Spotify</a>')     

		prettyCirclesTogether(data.lyrics);

  })
}


$("#test").on("click", searchSong);

var width = 750,
	height = 500;

var fill = d3.scale.category20();
  // var data = [{word:"Hello",weight:20},{word:"World",weight:10},{word:"Normally",weight:25},{word:"You",weight:15},{word:"Want",weight:30},{word:"More",weight:12},{word:"Words",weight:8},{word:"But",weight:18},{word:"Who",weight:22},{word:"Cares",weight:27}];

  var data = [{count: 15, word:'I'}, {count: 2, word:'the'}, {count: 16, word:'y'}, {count: 1, word:'to'}, {count: 5, word:'and'}, {count: 1, word:'a'}, {count: 7, word:'me'}, {count: 5, word:'it'}, {count: 5, word:'not'}, {count: 2, word:'in'}, {count: 1, word:'my'}, {count: 1, word:'your'}, {count: 1, word:'that'}, {count: 3, word:'do'}, {count: 2, word:'are'}, {count: 3, word:'am'}, {count: 4, word:'will'}, {count: 1, word:'for'}, {count: 1, word:'be'}, {count: 1, word:'have'}, {count: 1, word:'love'}, {count: 2, word:'know'}, {count: 1, word:'but'}, {count: 1, word:'with'}, {count: 1, word:'just'}, {count: 1, word:'when'}, {count: 1, word:'like'}, {count: 4, word:'come'}, {count: 1, word:'go'}, {count: 1, word:'up'}, {count: 1, word:'down'}, {count: 1, word:'see'}, {count: 6, word:'if'}, {count: 1, word:'got'}, {count: 7, word:'never'}, {count: 1, word:'want'}, {count: 3, word:'let'}, {count: 1, word:'make'}, {count: 1, word:'take'}, {count: 1, word:'here'}, {count: 4, word:'how'}, {count: 2, word:'caus'}, {count: 2, word:'tell'}, {count: 3, word:'again'}, {count: 1, word:'whi'}, {count: 1, word:'well'}, {count: 2, word:'wo'}, {count: 2, word:'still'}, {count: 1, word:'around'}, {count: 1, word:'did'}, {count: 1, word:'thought'}, {count: 1, word:'care'}, {count: 1, word:'hope'}, {count: 1, word:'sin'}, {count: 1, word:'breath'}, {count: 1, word:'sound'}, {count: 1, word:'might'}, {count: 1, word:'town'}, {count: 1, word:'ground'}, {count: 1, word:'wake'}, {count: 4, word:'guess'}, {count: 1, word:'blow'}, {count: 1, word:'win'}, {count: 1, word:'babe'}, {count: 1, word:'snow'}, {count: 1, word:'slide'}, {count: 1, word:'grin'}, {count: 1, word:'vow'}, {count: 1, word:'bride'}, {count: 1, word:'chin'}, {count: 1, word:'plug'}]

// var wordScale = d3.scale.linear().range([50,100]);

// 	wordScale.domain([
// 		d3.min(data, function(d) { return d.size; }),
// 		d3.max(data, function(d) { return d.size; })
// 	]);

d3.layout.cloud().size([width, height])
      .words(data.map(function(d) {
        return {text: d.word, size: d.count};
      }))
      .padding(0)
      .rotate(function() { return ~~(Math.random() * 2) * 90; })
      .font("Impact")
      .fontSize(function(d) { return (d.size * 20); })
      .on("end", draw)
      .start();


function draw(words) {
  d3.select("#d3-area").append("svg")
      .attr("width", width)
      .attr("height", height)
    .append("g")
      .attr("transform", "translate(" + (width / 2) + "," + (height / 2) + ")")
    .selectAll("text")
      .data(words)
    .enter().append("text")
      .style("font-size", function(d) { return d.size + "px"; })
      .style("font-family", "Impact")
      .style("fill", function(d, i) { return fill(i); })
      .attr("text-anchor", "middle")
      .attr("transform", function(d) {
        return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
      })
      .text(function(d) { return d.text; });
}



