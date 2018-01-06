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
	var tour_id = document.getElementById("tour_id").textContent
	var titles_th = document.getElementById("title_th")
	var title_th = titles_th.options[titles_th.selectedIndex].value
	var name_th = document.getElementById("name_th").value
	var surname_th = document.getElementById("surname_th").value
	var titles_en = document.getElementById("title_en")
	var title_en = titles_en.options[titles_en.selectedIndex].value
	var name_en = document.getElementById("name_en").value
	var surname_en = document.getElementById("surname_en").value
	var sex = ""
	if (document.getElementById("male").checked) {
		sex = document.getElementById("male").value
	}else if(document.getElementById("female").checked){
		sex = document.getElementById("female").value
	}
	var person_id = document.getElementById("personID").value
	var birthday = document.getElementById("birthday").value
	var email = document.getElementById("email").value
	var tel = document.getElementById("tel").value
	var countrys = document.getElementById("country")
	var country = countrys.options[countrys.selectedIndex].value
	var nationalitys = document.getElementById("nationality")
	var nationality = nationalitys.options[nationalitys.selectedIndex].value
	var address = document.getElementById("address").value
	var provinces = document.getElementById("province")
	var province = provinces.options[provinces.selectedIndex].value
	var post = document.getElementById("post").value
	var passport = document.getElementById("passport").value
	var issue_date = document.getElementById("issueDate").value
	var expire_date = document.getElementById("expireDate").value
	var detail = document.getElementById("detail").value
	var no_pig = "N"
	var no_meat = "N"
	var no_chicken = "N"
	var halal = "N"
	var mangsa = "N"
	var vegetarian = "N"
	var islam = "N"
	var no_seafood = "N"
	var no_shrimp = "N"
	var no_fish = "N"
	if(document.getElementById("no_pig").checked){
		no_pig = "Y"
	}
	if(document.getElementById("no_meat").checked){
		no_meat = "Y"
	}
	if(document.getElementById("no_chicken").checked){
		no_chicken = "Y"
	}
	if(document.getElementById("halal").checked){
		halal = "Y"
	}
	if(document.getElementById("mangsa").checked){
		mangsa = "Y"
	}
	if(document.getElementById("vegetarian").checked){
		vegetarian = "Y"
	}
	if(document.getElementById("islam").checked){
		islam = "Y"
	}
	if(document.getElementById("no_seafood").checked){
		no_seafood = "Y"
	}
	if(document.getElementById("no_shrimp").checked){
		no_shrimp = "Y"
	}
	if(document.getElementById("no_fish").checked){
		no_fish = "Y"
	}
	var json = JSON.stringify({"tour_id" :tour_id,
		"title_th" :title_th,
		"name_th" :name_th,
		"surname_th" :surname_th,
		"title_en" :title_en,
		"name_en" :name_en,
		"surname_en" :surname_en,
		"sex" : sex,
		"person_id" :person_id,
		"birthday" :birthday,
		"email" :email,
		"tel" :tel,
		"country" : country,
		"nationality" : nationality,
		"address" : address,
		"province" : province,
		"post" :post,
		"passport" :passport,
		"issue_date" :issue_date,
		"expire_date" :expire_date,
		"detail" :detail,
		"no_pig" : no_pig,
		"no_meat" : no_meat,
		"no_chicken" : no_chicken,
		"halal" : halal,
		"mangsa" : mangsa,
		"vegetarian" : vegetarian,
		"islam" : islam,
		"no_seafood" : no_seafood,
		"no_shrimp" : no_shrimp,
		"no_fish" : no_fish})
	xmlhttp.open("POST", "/api/update_tour")
	xmlhttp.setRequestHeader("Content-Type", "application/json ; charset=UTF-8" )
	xmlhttp.send(json)
}

function changeTittle() {
	var e = document.getElementById("title_th");
	var title_th = e.options[e.selectedIndex].value
	var title_en = ""
	if (title_th=="นาย") {
		title_en = "Mr."
		document.getElementById("male").checked = true
	} else if (title_th=="นาง") {
		title_en = "Mrs."
		document.getElementById("female").checked = true
	} else if (title_th=="นางสาว") {
		title_en = "Ms."
		document.getElementById("female").checked = true
	} else if (title_th=="เด็กชาย") {
		title_en = "Mstr."
		document.getElementById("male").checked = true
	} else if (title_th=="เด็กหญิง") {
		title_en = "Ms."
		document.getElementById("female").checked = true
	}
	var sex = ""
	document.getElementById("title_en").value = title_en

	console.log(country)
}

