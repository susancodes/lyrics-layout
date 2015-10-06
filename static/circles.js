function searchSong() {

  var url = "/songsearch"

  $.get(url, function (data){

      console.log(data);

      $("#song-title").text("Song Title: " + data.song_name);
      $("#song-artist").text("Artist: " + data.artist);      
      $("#song-genre").text("Genre: " + data.genre);      
      $("#song-spotify").html('<a href="' + data.spotify + '">Play Song on Spotify</a>')     

      makePrettyCircles(data.lyrics);
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
	

$("#test").on("click", searchSong);