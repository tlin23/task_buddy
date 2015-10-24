$(document).ready(function(){ 
	// $("div").css("border", "3px solid red");
	$("#merges").click(function(){merge_recent()});
	console.log("Please work")
});

function merge_recent() {
	alert("calling merge recent");
	$.ajax({
		url: '/giveData',
		type: 'GET',
		// dataType: 'default: Intelligent Guess (Other values: xml, json, script, or html)',
		// data: {param1: 'value1'},
	})
	.done(function() {
		console.log("success");
	})
	.fail(function() {
		console.log("error");
	})
	.always(function() {
		console.log("complete");
	});
	
}