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

function do_search(event) {
    buttons = $(":button").filter(".search-item");
    var searchStr = "";
    buttons.each(function(i) {
        searchStr += $(this).val() + " ";
    });
    searchStr += $(".searchField").val();
    $('.hiddenInput').val(searchStr);
    console.log("Search string is " + searchStr);
    console.log($('.hiddenInput').val());
    event.preventDefault();
    $.ajax({
        url : "/socketbox/search/",
        type : "POST",
        data : { search : searchStr },

        success : function(results) {
            console.log(results);
            $(".search-results").html(results);
        }
    });
}

$(document).ready(function() {
	$(".btn-search-term").on("click", function() {
		console.log($(this));
		$(this).hide();
	});
	$(".searchField").on("keyup", do_search);
	$(".submit").on("click", do_search);
});

// This function gets cookie with a given name
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

/*
The functions below will create a header with csrftoken
*/

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

createSearchBubbles();



//TODO 
//this is the search results area
//<a href="#" class="list-group-item"><img alt="logo" src="../../static/images/logo.png" width="30" height="30" class= "pull-left">%toolName%,%ownerName%</a>




