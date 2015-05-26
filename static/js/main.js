//var searchWords = [$("input[name=searchQueryJUSTIN]")];// swap this with the line below it when it works
var searchWords = "saw rotary";// swap this with the line above it when it works
var searchArray = searchWords.split(" ");


createSearchBubbles = function(){
	var i = 0;
	while (i < searchArray.length){
		var HTMLtoolDescr = '<button type="button" class="btn btn-info btn-xs" id= "tag#"><span class="glyphicon glyphicon-remove"></span> %searchWord%</button>';
		var intermtoolDescr = HTMLtoolDescr.replace("#", i);
		var formattedtoolDescr = intermtoolDescr.replace("%searchWord%", searchArray[i]);
		$(".searchTerms").append(formattedtoolDescr);
		i++;
	}
}


$(document).ready(function() {
	$(".btn-info").on("click", function() {
		console.log($(this));
		$(this).hide();
	});
});



createSearchBubbles();



