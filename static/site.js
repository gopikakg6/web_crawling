function build_lyrics(lyrics){
    ret = $(`<p>
        <h4>Lyrics for ${lyrics.name}</h4>
        <h5><small class="text-muted">${lyrics.artist.name}</small></h5>
    </p>)
<p>
    ${lyrics.lyrics}
</p>`)

    return ret;
}



function main() {
    $("a.songlink").click(func)
};
function func(ev) {
    ev.preventDefault();
    $("div.lyrics").text("Loading......")
    $.ajax({
        url: ev.target.href,
        dataType: 'json',
        success: function (data, textStatus, jqXHR) {
            $("div.lyrics").html(build_lyrics(data.song));
            var text = ev.target.innerText;
            var parent = ev.target.parentNode;
            $(parent).html(text)
            $(".songname")
                .html(`<a class = "songlink" href="/song/${$(".songname")
                .attr("id")}">${$(".songname").text()}<a/>`);
            $(".songname a").click(func);
            $(".songname").attr("class", "songlinks");
            $(parent).attr("class", "songname");
        }
    })
}
$(main);










    


