function setData() {
	document.getElementById('paymentType').value="{{ data["PAYMENT_NAME"] }}"
	document.getElementById('bank').value="{{ data["CHEQUE_BANK"] }}"

	document.getElementById('saleID').disabled=true
	document.getElementById('saleName').disabled=true
	document.getElementById('tourName').disabled=true
	document.getElementById('searchCustomer').disabled=true
	document.getElementById('clearHead').disabled=true
	// document.getElementById('address').disabled=true

	document.getElementById('paymentVat').disabled=true
	document.getElementById('paymentNoVat').disabled=true
	document.getElementById('totalNoVat').disabled=true
	document.getElementById('vat').disabled=true
	document.getElementById('totalAll').disabled=true

	var paymentType = {{data["PAYMENT_NAME"]}}
	if (paymentType==01) {
		document.getElementById("bank").disabled = false; 		
		document.getElementById("chequeNo").disabled = false; 
		document.getElementById("chequeDate").disabled = false; 
		
	}else{
		document.getElementById("bank").disabled = true; 
		document.getElementById("chequeNo").disabled = true; 
		document.getElementById("chequeDate").disabled = true; 

	}
}
