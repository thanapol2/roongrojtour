$(document).ready(function() {
	var table = $('#example').DataTable({
		"columnDefs": [ {
			"targets": -1,
			"data": null,
			"defaultContent": "<button>View/Edit</button>"
		} ]
		
	});

	$('#dropdown1').on('change', function () {
		table.columns(3).search( this.value ).draw();
	} );
	$('#example tbody').on( 'click', 'button', function () {
		var data = table.row( $(this).parents('tr') ).data();
		document.location.href = "/api/search_tour/"+data[0]
	} );
	// $('#example tbody').on( 'dblclick', 'tr', function (e) {
	// 	var id = table.row( $(this).parents('tr') ).data();
	// 	alert(id);
	// 	// var test = dataTable.rows(this).select()
	// 	// var data = table.row( $(this).parents('tr') ).data();
	// } );
} );
function clickNewTour(){
	document.location.href = "/api/new_tour"
}
function clickNewCompany(){
	document.location.href = "/api/new_company"
}