String.prototype.getKey = function() {
	return this.slice(-8)
}

$(document).ready(function(){
	$( "#link" ).click(function() {										//when link is clicked
		var addressValue = $(this).attr("href");						//jquery gets the href attr of link and js sets addressValue equal to this
		addressValue = addressValue.getKey();							//getKey function gets the last 8 char's of href
		$.get("/getmethod/<" + addressValue + ">", function(data){		//ajax calls the getmethod, "data" is returned from route and passed into anonymous js function
			$("#hit_count").text(data);									//jQuery sets texts of #hit_count node to data
		});
	});
});