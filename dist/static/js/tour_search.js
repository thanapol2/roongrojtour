$(document).ready(function() {
	var table = $('#example').DataTable();
	$('#dropdown1').on('change', function () {
		table.columns(3).search( this.value ).draw();
	} );
} );
