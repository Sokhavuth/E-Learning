//static/scripts/index.js
class Index{
  constructor(){
    this.page = 0;
  }

  navigate(nav){
    $('#front-nav .home').attr('src', '/static/images/loading.gif')
    $.get("/panel",
    {nav:nav},
    function(data, status){
      if(status == "success"){
        var html = '';
        var data = JSON.parse(data);
        
        if((data.posts).length !== 0){
          for(var v in data.posts){
            if(v == 0){
              html += '<div class="wrapper1">';
              html += '<div  style="position:relative;padding-top:57.30%;">';
            }else{
              html += '<div class="wrapper">';
              html += '<div  style="position:relative;padding-top:56.25%;">';
            }

            html += `<a href="/post/${ data['posts'][v][0] }"><img src="${ data['thumbs'][v] }" style="position:absolute;top:0;left:0;width:100%;min-height:100%;" /></a>`;
            html += `<a href="/post/${ data['posts'][v][0] }"><p class="title" >${ data['posts'][v][1] }</p></a>`;

            if (data['videos'][v].length){
              html += `<a href="/post/${ data['posts'][v][0] }"><img class="play-icon" src="/static/images/play.png" /></a>`;
            }

            html += `<p class="date-news" >${(data['posts'][v][4]) }</p>`;
            html += '</div>';
            html += '</div>';
          }

          $('#front-panel').html(html);
        }

        $('#front-nav .home').attr('src', '/static/images/home.png')
        
      }else
        alert('Fail to connect to server.');
    });
  }

  loadBook(){
    $('#load-more img').attr('src', '/static/images/loading.gif');
    index.page += 1;

    $.get('/book/load/',
      {'ajax':index.page},
      function(data, status){
        if(status === "success"){
          var html = "";
          for(var v=0; v<data['books'].length; v++){
            html += `<a href="/book/${ data['books'][v][0] }"><img src="${ data['thumbs'][v] }" /></a>`;
          }

          $('#books').append(html);
          $('#load-more img').attr('src', '/static/images/load-more.png');

        }else{
          alert('Fail to connect to server.');
        }
    });
  }

}//End of class

const index = new Index();