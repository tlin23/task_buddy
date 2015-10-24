$(document).ready(function(){ 
	// $("div").css("border", "3px solid red");
	$("button").click(function(){getData()});

});

function AlertMe(things) {
	alert(things);

}

function getData() {
	alert("getting data")
	$.ajax({
		url: "/giveData", 
		type: 'GET',
	    error: function() {
	        alert( "ajax error" );
	    },
	    success: function(response) {
	        alert( "ajax success");
	        console.log(response);
	        $("#responseBox").append(response);
	    }})
}