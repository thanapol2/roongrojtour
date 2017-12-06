$(function(){
	$('#submit').click(function(){
		var formData = new FormData();
		formData.append('name_th', $('#name_th').val());
		$.ajax({
			url: '/api/update_tour',
			// data: formData
			data: JSON.stringify({"name_th" : $('#name_th').val()}),
			type: 'POST',
			processData: false,
			contentType: 'application/json; charset=UTF-8',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});

