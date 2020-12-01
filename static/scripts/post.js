//static/scripts/post.js
class Post{
  setVideo(video){
    var video = JSON.parse(video);
    
    if(video.vidType === "youtube"){
      var src = "https://www.youtube.com/embed/" + video.videoId;
    }else if(video.vidType === "fbvid"){
      var src = `https://www.facebook.com/watch/?v=${video.videoId}`;
    }else if(video.vidType === "googledrive"){
      var src = "https://docs.google.com/file/d/"+video.videoId+"/preview";
    }else if(video.vidType === "dailymotion"){
      var src = "https://www.dailymotion.com/embed/video/" + video.vidType;
    }else if(video.vidType === "vimeo"){
      var src = "https://player.vimeo.com/video/" + video.vidType;
    }else if(video.vidType === "okvid"){
      var src = "//ok.ru/videoembed/" + video.vidType;
    }else if(video.vidType === "youtubepl"){
      var src = "https://www.youtube.com/embed/videoseries?list=" + video.vidType;
    }

    if(video.vidType !== 'fbvid'){
      var iframe = `<div style='position:relative;padding-top:56.25%;margin-top:20px;'>
      <iframe id="video-player" src="${src}" frameborder="0" allowfullscreen></iframe>
      </div>`;
    }else{
      var iframe = `<div class="fb-video" data-href="${src}" data-width="auto" data-show-captions="true"></div>`;
    }

    $('#video-wrapper').html(iframe);
  }
}//End of class

const post = new Post();