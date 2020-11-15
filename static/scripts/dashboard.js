//static/scripts/dashboard.js
class Lib{
  load_items(url){
    $('#load-more img').attr('src', '/static/images/loading.gif');
    $.get(url, function(data, status){
      if(status == "success"){
        listing_items(data);
      }else{
        alert('Fail to connect to server.');
      }
    });
  }
}//End class