function setData() {
	
	var vat = {{data["VAT"]}}
	if (vat!=0) {
		document.getElementById("vatCal").checked = true
		
	}else{
		
		document.getElementById("noVat").checked = true
	}

	document.getElementById("salesID").disabled = true
	document.getElementById("salesName").disabled = true
	document.getElementById("issueDate").disabled = true
	document.getElementById("due").disabled = true

	document.getElementById("ref").disabled = true
	document.getElementById("subject").disabled = true

	document.getElementById("tourName").disabled = true
	
	document.getElementById("taxID").disabled = true
	document.getElementById("tel").disabled = true
	document.getElementById("email").disabled = true
	document.getElementById("attention").disabled = true
	document.getElementById("address").disabled = true

	document.getElementById("addBtn").disabled = true
	document.getElementById("clearDetail").disabled = true

	document.getElementById("vatCal").disabled = true
	document.getElementById("adjustVat").disabled = true
	document.getElementById("noVat").disabled = true


	$('button[type="remove"]').prop('disabled', true)
}
