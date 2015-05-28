//var searchWords = [$("input[name=searchQueryJUSTIN]")];// swap this with the line below it when it works
var searchWords = "saw";// swap this with the line above it when it works
var searchArray = searchWords.split(" ");

var SearchBubbles = {

	mainSearchInput: function () {
		this.i = 0;
		if (searchArray.length > -1 && searchArray[0] != false){
			while (this.i < searchArray.length){
				//format the html with string replacement
				var htmlBase = '<button type="button" class="btn btn-info btn-xs btn-search-term" id= "tag#"><span class="glyphicon glyphicon-remove"></span> %searchWord%</button>';
				htmlBase = htmlBase.replace("#", this.i);
				this.formattedHTML = htmlBase.replace("%searchWord%", searchArray[this.i]);
				//send the html to index
				$(".searchTerms:last").append(this.formattedHTML);
				this.i++;
				this.remove();
			}
		}else{
			//continue;
		};
	},

	helperTerms: function () {
		$(".searchHelpers").on("click", function () {
			//add enumerated #id to each button
			if ($(".searchTerms").children().length < 0){
				var elemNum = 0;
			}else{
				var elemNum = $(".searchTerms").children().length;
			}
			//format the html with string replacement
			var htmlBase = '<button type="button" class="btn btn-info btn-xs btn-search-term" id= "tag#"><span class="glyphicon glyphicon-remove"></span> %searchWord%</button>';
			htmlBase = htmlBase.replace("#", elemNum);
			this.formattedHTML = htmlBase.replace("%searchWord%", $(this).text());
			//send the html to index
			$(".searchTerms:last").append(this.formattedHTML);
			SearchBubbles.remove();
		});
	},

	remove: function () {
		$(".btn-search-term").on("click", function() {
			//console.log(this);
			$(this).hide();
		});
	}
}

SearchBubbles.mainSearchInput();
SearchBubbles.helperTerms();




// $(".submit").on("click", function() {
// 	var buttons = $(":button").filter(".search-search-term");
// 	var searchStr = "";
// 	for(i = 0; i < buttons.length; i++) {
// 		searchStr += buttons[i].value + " ";
// 	}
// 	$('.hiddenInput').val(searchStr);
// 	console.log("Search string is " + searchStr);
// 	console.log($('.hiddenInput').val());
// });



//TODO 
//this is the search results area
//<a href="#" class="list-group-item"><img alt="logo" src="../../static/images/logo.png" width="30" height="30" class= "pull-left">%toolName%,%ownerName%</a>




