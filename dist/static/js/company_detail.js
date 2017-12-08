// $(function(){
// 	$('#submit').click(function(){
// 		$.ajax({
// 			url: '/api/update_tour',
// 			// data: formData
// 			data: JSON.stringify({"name_th" : $('#name_th').val()}),
// 			type: 'POST',
// 			processData: false,
// 			contentType: 'application/json; charset=UTF-8',
// 			success: function(response){
// 				console.log(response);
// 			},
// 			error: function(error){
// 				console.log(error);
// 			}
// 		});
// 	});
// });

function clickSubmit(){
	var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance 
	var json = JSON.stringify({"name_th":"สมหญิง"})
	xmlhttp.open("POST", "/api/update_tour");
	xmlhttp.setRequestHeader("Content-Type", "application/json ; charset=UTF-8" );
	xmlhttp.send(json);
}
function changeTittle() {
    var e = document.getElementById("title_th");
    var title_th = e.options[e.selectedIndex].value;
    // var title_en = document.getElementById('title_en');
	document.getElementById("title_en").value = "Ms.";
}

