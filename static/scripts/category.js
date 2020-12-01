//static/scripts/category.js
class Category{
  constructor(){
    this.page = 0;
  }

  loadPost(label){
    $('#load-more img').attr('src', '/static/images/loading.gif');
    category.page += 1;
    
    $.get('/post/load/ajax/'+label, 
    {'ajax':category.page}
    ,function(data, status){
      if(status === "success"){
        var html = "";
        
        for(var v=0; v<data['posts'].length; v++){
          html += `<div class="post-wrapper">`;
          html += `<a class="wrapper" href="/post/${data['posts'][v][0]}">`;
          html += `<img src="${ data['thumbs'][v] }" />`;
          if(data['videos'][v]){
            html += `<img class="play-icon" src="/static/images/play.png" />`;
          }
          html += `<p class="post-date">${ data['posts'][v][4] }</p>`;
          html += `</a>`;
          html += `<a class="post-title" href="/post/${ data['posts'][v][0] }">${ data['posts'][v][1] }</a>`;
          html += `</div>`;
        }

        $('#container').append(html);
        $('#load-more img').attr('src', '/static/images/load-more.png');

      }else{
        alert('Fail to connect to server.');
      }
    });
  }
}//End of class

const category = new Category();
