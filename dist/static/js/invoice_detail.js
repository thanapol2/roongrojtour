// var vat_type = 1
$(document).ready(function() {
  var table = $('#tableDetail').DataTable({
    "bSort" : false,
    "bFilter" : false,
    "bPaginate" : false,
    "columnDefs": [ {
      "targets": 0,
      "data": null,
      "defaultContent": '<button type="button" id="remove">Delete</button>'
    } ]
  });

  $('#addBtn').on( 'click', function () {
    if($('#sum').val()==0){
      alert("ไม่สามารถเพิ่ม รายละเอียดได้เนื่องจาก ราคารวมเท่ากับ 0");
    }else{
      table.row.add( [
        '',
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
    }
  });

  $('#tableDetail tbody').on( 'click', '#remove', function () {
    var row = table.row( $(this).parents('tr') );
    row.remove().draw( false );
    var totalRecords = table.page.info().recordsTotal
    var sumColumn = 0
    if(totalRecords ==0){
      sumColumn = 0
    }else {
      sumColumn = table.column(5).data().reduce(function(a,b){
        return parseInt(a)+parseInt(b);
      })
    }
    
    $('#totalAll').val(parseFloat(sumColumn).toFixed(2))
  } );

  $("#input_form").submit(function(e) {
    e.preventDefault();
    var totalRecords = table.page.info().recordsTotal
    if(totalRecords ==0){
      alert("ไม่มีข้อมูลรายละเอียด");
    }else{

    }
    // clickSubmit()
  });

});

function calSumRow() {
  var qty = document.getElementById("qty").value;
  var price = document.getElementById("price").value;
  document.getElementById("sum").value = price*qty;
}

function clearInput() {
  document.getElementById("service").value = ''
  document.getElementById("invoiceType").value = ''
  document.getElementById("qty").value = ''
  document.getElementById("price").value = ''
  document.getElementById("sum").value = ''
}

function vatOptions(myRadio) {
    // 1 vatcal , 2 adjust, 3no vat
    var vat_type = myRadio.value;
    if(vat_type ==2){
      document.getElementById("vat").disabled=false
    }else if(vat_type ==3 ){
      document.getElementById("vat").value = '0.00'
      document.getElementById("vat").disabled=true
    }
    
}
