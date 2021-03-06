
$(document).ready(function() {
  var table = $('#example').DataTable({
   "columnDefs": [ {
    "targets": -1,
    "data": null,
    "defaultContent": "<button>View/Edit</button>"
  } ,
  {
    'targets': 0,
    'searchable': false,
    'orderable': false,
    'width': '1%',
    'className': 'dt-body-center',
    'render': function (data, type, full, meta){
     return '<input type="checkbox">';
   }
 }],
 "order": [[ 1, 'asc' ]]
});
  $('#dropdown1').on('change', function () {
    table.draw();
  } );
  $('#startDate, #endDate').change(function () {
    table.draw();
  });
  $.fn.dataTable.ext.search.push(
    function (settings, data, dataIndex) {
      var min = new Date($('#startDate').val())
      var max = new Date($('#endDate').val())
      var type = $('#dropdown1').val()
      var result = true
      var startDate = new Date(data[4]);
      if (data[1].search(type) == 0){
        result = true;
      }else{
        result = false;
      }
      if (isNaN(min) && isNaN(max)) { return true && result; }
      if (isNaN(min) && startDate <= max) { return true && result;}
      if(isNaN(max) && startDate >= min) {return true && result;}
      if (startDate <= max && startDate >= min) { return true && result; }
      return false;
    }
    );
  $('#example tbody').on( 'click', 'button', function () {
    var data = table.row( $(this).parents('tr') ).data();
    document.location.href = "/api/invoice/"+data[1]
  } );

  // Event listener to the two range filtering inputs to redraw on input
});

function clickNewRT(){
  document.location.href = "/api/rtinvoice"
}
function clickNewRTS(){
  document.location.href = "/api/rtsinvoice"
}
