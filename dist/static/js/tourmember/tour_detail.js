$(document).ready(function(){
	$("#input_form").submit(function(e) {
		e.preventDefault();
		var status = $("#status").text();
		if(("OK"==status)||(" "==status)){
			clickSubmit()
		}else{
			alert("Please, Check TH_NAME and TH_SURNAME");
		}
	});
	$("#name_th").keyup(function(){
		checkNameSurname()

	});
	$("#surname_th").keyup(function(){
		checkNameSurname()
	});
});

function readURL(input) {
	if (input.files && input.files[0]) {
		var reader = new FileReader();

		reader.onload = function (e) {
			$('#img_display')
			.attr('src', e.target.result)
		};

		reader.readAsDataURL(input.files[0]);
	}
}

function checkNameSurname(){
	var name_th = document.getElementById("name_th").value
	var surname_th = document.getElementById("surname_th").value
	if((name_th.length==0)||(surname_th.length==0)){
		return;
	}else{
		var xmlhttp = new XMLHttpRequest();
		xmlhttp.onreadystatechange = function() {
			if (this.readyState == 4 && this.status == 200) {
				document.getElementById("status").innerHTML = this.responseText;
			}
		};
		xmlhttp.open("GET", "/api/checked_name/" + name_th+"_"+surname_th, true);
		xmlhttp.send();
	}
}


function clickSubmit(){
	var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance 
	xmlhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			alert(this.responseText)
		}
	};
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
	// var path_pic = document.getElementById("input_img").value
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
	var json = JSON.stringify({"TOUR_ID" :tour_id,
		"THAI_TITLE" :title_th,
		"THAI_NAME" :name_th,
		"THAI_SURNAME" :surname_th,
		"ENG_TITLE" :title_en,
		"ENG_NAME" :name_en,
		"ENG_SURNAME" :surname_en,
		"SEX" : sex,
		"PERSON_ID" :person_id,
		"BIRTH_DAY" :birthday,
		"EMAIL" :email,
		"TEL" :tel,
		"COUNTRY" : country,
		"NATIONALITY" : nationality,
		"ADDRESS" : address,
		"PROVINCE" : province,
		"POST_NO" :post,
		"PASSPORT_ID" :passport,
		"ISSUE_DATE" :issue_date,
		"EXPIRE_DATE" :expire_date,
		"DETAIL" :detail,
		"NO_PIG" : no_pig,
		"NO_MEAT" : no_meat,
		"NO_CHICKEN" : no_chicken,
		"HALAL" : halal,
		"MANGSA" : mangsa,
		"VEGETARIAN" : vegetarian,
		"ISLAM" : islam,
		"NO_SEAFOOD" : no_seafood,
		"NO_SHRIMP" : no_shrimp,
		"NO_FISH" : no_fish})
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
}

