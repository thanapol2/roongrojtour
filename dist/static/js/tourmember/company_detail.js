$(document).ready(function(){
	$("#input_form").submit(function(e) {
		e.preventDefault();
		clickSubmit()
	});
})

function clickSubmit(){
	var xmlhttp = new XMLHttpRequest();   
	xmlhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			alert(this.responseText)
		}
	};
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



	var json = JSON.stringify({"COMPANY_ID" :company_id,
		"THAI_NAME" :name_th,
		"ENG_NAME" :name_en,
		"TAX_ID" :tax_id,
		"COMPANY_TYPE" :company_type,
		"EMAIL" :email,
		"TEL_NO" :tel,
		"ADDRESS" : address,
		"PROVINCE" : province,
		"POST_NO" :post,
		"REMARK" :detail})

	xmlhttp.open("POST", "/api/update_company")
	xmlhttp.setRequestHeader("Content-Type", "application/json ; charset=UTF-8" )
	xmlhttp.send(json)
}

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
