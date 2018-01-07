
$(document).ready(function() {
  var table = $('#example').DataTable({
    "bSort" : false
  });
  $('#addBtn').on( 'click', function () {
    table.row.add( [
      '<button type="button" id="remove">Delete</button>',
      $('#service').val(),
      $('#invoiceType').val(),
      $('#qty').val(),
      $('#price').val(),
      $('#sum').val()
      ] ).draw( false );
    var sumColumn = table.column(5).data().reduce(function(a,b){
      return parseInt(a)+parseInt(b);
    })
    $('#totalAll').val(parseFloat(sumColumn).toFixed(2))
  });
  $('#example tbody').on( 'click', '#remove', function () {
    var row = table.row( $(this).parents('tr') );
    row.remove().draw( false );
    var sumColumn = table.column(5).data().reduce(function(a,b){
      return parseInt(a)+parseInt(b);
    })
    $('#totalAll').val(parseFloat(sumColumn).toFixed(2))
  } );
});

function calSumRow() {
  var qty = document.getElementById("qty").value;
  var price = document.getElementById("price").value;
  document.getElementById("sum").value = price*qty;
}