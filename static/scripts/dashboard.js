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
        }else if(type === 'pages'){
          lib.listing_pages(data);
        }else if(type === 'books'){
          lib.listing_books(data);
        }else if(type === 'users'){
          lib.listing_users(data);
        }
      }else{
        alert('Fail to connect to server.');
      }
    });
  }

  listing_users(data){
    var html = '';
    for(var v=0; v<data['users'].length; v++){
      html += '<li class="user">';
      html += `<a class="thumbnail" href="/user/${ data['users'][v][0] }"><img src="${data['thumbs'][v]}" /></a>`;
      html += `<div class='title'>`;
      html += `<a href="/user/${ data['users'][v][0] }">${ data['users'][v][1] }</a>`;
      html += `<span>${ data['users'][v][3] }</span>`;
      html += `</div>`;
      html += `<div class="crud">`;
      html += `<a class="user">${ data['users'][v][7] }</a>`;
      html += `<a href='/dashboard/user/delete/${ data["users"][v][0] }'><img src="/static/images/delete.png" /></a>`;
      html += `<a href='/dashboard/user/edit/${ data["users"][v][0] }'><img src="/static/images/edit.png" /></a>`;
      html += `</div>`;
      html += `</li>`;
    }

    $('#item-listing').append(html);
    $('#load-more img').attr('src', '/static/images/load-more.png')
  }

  listing_books(data){
    var html = '';
    for(var v=0; v<data['books'].length; v++){
      html += '<li class="book">';
      html += `<a class="thumbnail" href="/book/${ data['books'][v][0] }"><img src="${data['thumbs'][v]}" /></a>`;
      html += `<div class='title'>`;
      html += `<a href="/book/${ data['books'][v][0] }">${ data['books'][v][1] }</a>`;
      html += `<span>${ data['books'][v][3] }</span>`;
      html += `</div>`;
      html += `<div class="crud">`;
      html += `<a class="user">${ data['books'][v][5] }</a>`;
      html += `<a href='/dashboard/book/delete/${ data["books"][v][0] }'><img src="/static/images/delete.png" /></a>`;
      html += `<a href='/dashboard/book/edit/${ data["books"][v][0] }'><img src="/static/images/edit.png" /></a>`;
      html += `</div>`;
      html += `</li>`;
    }

    $('#item-listing').append(html);
    $('#load-more img').attr('src', '/static/images/load-more.png')
  }

  listing_pages(data){
    var html = '';
    for(var v=0; v<data['pages'].length; v++){
      html += '<li class="page">';
      html += `<a class="thumbnail" href="/page/${ data['pages'][v][0] }"><img src="${data['thumbs'][v]}" /></a>`;
      html += `<div class='title'>`;
      html += `<a href="/page/${ data['pages'][v][0] }">${ data['pages'][v][1] }</a>`;
      html += `<span>${ data['pages'][v][3] }</span>`;
      html += `</div>`;
      html += `<div class="crud">`;
      html += `<a class="user">${ data['pages'][v][5] }</a>`;
      html += `<a href='/dashboard/page/delete/${ data["pages"][v][0] }'><img src="/static/images/delete.png" /></a>`;
      html += `<a href='/dashboard/page/edit/${ data["pages"][v][0] }'><img src="/static/images/edit.png" /></a>`;
      html += `</div>`;
      html += `</li>`;
    }

    $('#item-listing').append(html);
    $('#load-more img').attr('src', '/static/images/load-more.png')
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
    alert('វីដេអូ​ត្រូវ​បាន​បញ្ចូល​ទៅ​ក្នុង​ការផ្សាយ​។')
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