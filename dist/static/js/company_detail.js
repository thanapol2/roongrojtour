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
	var company_id = document.getElementById("company_id").textContent
	var name_th = document.getElementById("name_th").value
	var name_en = document.getElementById("name_en").value
	var tax_id = document.getElementById("taxID").value
	var types = document.getElementById("company_type")
	var company_type = types.options[types.selectedIndex].value
	var email = document.getElementById("email").value
	var tel = document.getElementById("tel").value
	var address = document.getElementById("address").value
	var provinces = document.getElementById("province")
	var province = provinces.options[provinces.selectedIndex].value
	var post = document.getElementById("post").value
	var detail = document.getElementById("detail").value

	

	var json = JSON.stringify({"company_id" :company_id,
		"name_th" :name_th,
		"name_en" :name_en,
		"tax_id" :tax_id,
		"company_type" :company_type,
		"email" :email,
		"tel" :tel,
		"address" : address,
		"province" : province,
		"post" :post,
		"detail" :detail})

	xmlhttp.open("POST", "/api/update_company")
	xmlhttp.setRequestHeader("Content-Type", "application/json ; charset=UTF-8" )
	xmlhttp.send(json)
}
function changeTittle() {
    var e = document.getElementById("title_th");
    var title_th = e.options[e.selectedIndex].value;
    // var title_en = document.getElementById('title_en');
	document.getElementById("title_en").value = "Ms.";
}

