//static/scripts/dashboard.js
class Lib{
  load_items(url, type){
    $('#load-more img').attr('src', '/static/images/loading.gif');
    $.get(url, function(data, status){
      if(status === "success"){
        if(type === "categories"){
          lib.listing_categories(data);
        }else if(type === "posts"){
          lib.listing_posts(data);
        }
      }else{
        alert('Fail to connect to server.');
      }
    });
  }

  listing_posts(data){
    var html = '';
    for(var v=0; v<data['posts'].length; v++){
      html += '<li class="post">';
      if(data['posts'][v][7].length){
        html += `<a class="thumbnail" href="/post/${ data['posts'][v][0] }">
        <img src="${data['thumbs'][v]}" />
        <img class="play-icon" src="/static/images/play.png" />
        </a>`;
      }else{
        html += `<a class="thumbnail" href="/post/${ data['posts'][v][0] }"><img src="${data['thumbs'][v]}" /></a>`;
      }
      html += `<div class='title'>`;
      html += `<a href="/post/${ data['posts'][v][0] }">${ data['posts'][v][1] }</a>`;
      html += `<span>${ data['posts'][v][4] }</span>`;
      html += `</div>`;
      html += `<div class="crud">`;
      html += `<a class="user">${ data['posts'][v][6] }</a>`;
      html += `<a href='/dashboard/post/delete/${ data["posts"][v][0] }'><img src="/static/images/delete.png" /></a>`;
      html += `<a href='/dashboard/post/edit/${ data["posts"][v][0] }'><img src="/static/images/edit.png" /></a>`;
      html += `</div>`;
      html += `</li>`;
    }

    $('#item-listing').append(html);
    $('#load-more img').attr('src', '/static/images/load-more.png')
  }

  listing_categories(data){
    var html = '';
    for(var v=0; v<data['categories'].length; v++){
      html += '<li class="category">';
      html += `<a class="thumbnail" href="/category/${ data['categories'][v][1] }"><img src="${data['thumbs'][v]}" /></a>`;
      html += `<div class='title'>`;
      html += `<a href="/category/${ data['categories'][v][1] }">${ data['categories'][v][1] }</a>`;
      html += `<span>${ data['categories'][v][3] }</span>`;
      html += `</div>`;
      html += `<div class="crud">`;
      html += `<a class="user">${ data['categories'][v][5] }</a>`;
      html += `<a href='/dashboard/category/delete/${ data["categories"][v][1] }'><img src="/static/images/delete.png" /></a>`;
      html += `<a href='/dashboard/category/edit/${ data["categories"][v][1] }'><img src="/static/images/edit.png" /></a>`;
      html += `</div>`;
      html += `</li>`;
    }

    $('#item-listing').append(html);
    $('#load-more img').attr('src', '/static/images/load-more.png')

  }

  getVideoForm(event){
    event.preventDefault();
    var json = {};
    var vidType = $("input:radio[name=vid-type]:checked").val();
    var videoId = $("input:text[name=video-id]").val();
    if($('#playlist').is(":checked")){ 
      var playlist = $("input:text[name=vid-title]").val();
    }

    json.vidType = vidType;
    json.videoId = videoId;
    json.playlist = playlist;

    $("input:hidden[name=fvidata]").val(JSON.stringify(json));
  }

  enable(){
    if($('#playlist').is(":checked")){     
      $("input:text[name=vid-title]").attr('disabled', false);   
    }else{     
      $("input:text[name=vid-title]").attr('disabled', true);
    } 
  }
}//End class

const lib = new Lib();