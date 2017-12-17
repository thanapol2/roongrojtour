
$(document).ready(function() {
	var table = $('#example').DataTable();
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
      var startDate = new Date(data[3]);
      if (data[0].search(type) == 0){
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

  // Event listener to the two range filtering inputs to redraw on input
});
