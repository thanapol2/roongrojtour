// var vat_type = 1
$(document).ready(function() {
  var table = $('#tableDetail').DataTable({
    "bSort" : false,
    "bFilter" : false,
    "bPaginate" : false,
    "columnDefs": [ {
      "targets": 0,
      "data": null,
      "defaultContent": '<button type="remove" id="remove">Delete</button>'
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
        $('#qty').val(),
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
  if(document.getElementById("invoiceType").value=='Discount'){
    document.getElementById("sum").value = price*qty*-1;
  }else{
    document.getElementById("sum").value = price*qty;
  }
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

function revised(){
  document.getElementById("salesID").disabled = false
  document.getElementById("salesName").disabled = false
  document.getElementById("issueDate").disabled = false
  document.getElementById("due").disabled = false

  document.getElementById("ref").disabled = false
  document.getElementById("subject").disabled = false

  document.getElementById("tourName").disabled = false

  document.getElementById("taxID").disabled = false
  document.getElementById("tel").disabled = false
  document.getElementById("email").disabled = false
  document.getElementById("attention").disabled = false
  document.getElementById("address").disabled = false

  document.getElementById("addBtn").disabled = false
  document.getElementById("clearDetail").disabled = false

  document.getElementById("vatCal").disabled = false
  document.getElementById("adjustVat").disabled = false
  document.getElementById("noVat").disabled = false
  $('button[type="remove"]').prop('disabled', false)
}

function changeTittle() {
  var e = document.getElementById("invoiceType");
  var invoiceType = e.options[e.selectedIndex].value
  var qty = document.getElementById("qty").value;
  var price = document.getElementById("price").value;
  if (invoiceType=="Discount") {
    document.getElementById("sum").value = price*qty*-1;
  } else {
    document.getElementById("sum").value = price*qty;
  }
}
