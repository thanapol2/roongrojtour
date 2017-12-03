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
} );
