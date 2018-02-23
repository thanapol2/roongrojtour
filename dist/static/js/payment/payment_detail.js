
$(document).ready(function() {

	$("#input_form").submit(function(e) {
		e.preventDefault();
    // clickSubmit()
});

});

function changePayment() {
	var e = document.getElementById("paymentType");
	var paymentType = e.options[e.selectedIndex].value
	var bank = "None"
	var chequeNo = "None"
	var chequeDate = ""
	if (paymentType==01) {
		document.getElementById("bank").disabled = false; 		
		document.getElementById("chequeNo").disabled = false; 
		document.getElementById("chequeDate").disabled = false; 
		
	}else{
		document.getElementById("bank").disabled = true; 
		document.getElementById("chequeNo").disabled = true; 
		document.getElementById("chequeDate").disabled = true; 
		document.getElementById("bank").value = bank
		document.getElementById("chequeNo").value = chequeNo
		document.getElementById("chequeDate").value = chequeDate
	}


}