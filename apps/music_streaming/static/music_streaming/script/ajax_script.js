function sideBarClickOff(){
    $('#main_content').html('');
    $('#left_sidebar').removeClass('blackOut');
    $('#left_sidebar').addClass('gradient');
    $('h2').not('.search_bar').removeClass('hover select');
    $('h2').not(this).addClass('stable');
    $(this).removeClass('hover stable');
    $(this).not('.search_bar').addClass('select');
    $('#magnify_glass').attr('src', '/static/music_streaming/img/search_magnifying_glass_icon.png');
    $('#magnify_glass').attr('alt-hover', '/static/music_streaming/img/search_magnifying_glass_icon_hover.png');
    $('h2.search_bar').addClass('stable');
    $('h2.search_bar').removeClass('select');
}
$(document).ready(function(){
    $('#big_search').keyup(function () {
        $('#big_search').attr('value') = '';
    });
    $('.search').mouseenter(function(){
        if ($('.search_bar').hasClass('stable')){
            var temp = $('#magnify_glass').attr('src');
            $('#magnify_glass').attr('src', $('#magnify_glass').attr('alt-hover'));
            $('#magnify_glass').attr('alt-hover', temp);
            $('h2.search_bar').addClass('hover');
            
        };
    }); 
    $('.search').mouseleave(function(){
        if ($('.search_bar').hasClass('hover')){
            var temp = $('#magnify_glass').attr('src');
            $('#magnify_glass').attr('src', $('#magnify_glass').attr('alt-hover'));
            $('#magnify_glass').attr('alt-hover', temp);
            $('h2.search_bar').removeClass('hover');
            
        }
    }); 
    $('.search').click(function(){
        console.log('search bar was clicked!')
        temp = $('#magnify_glass').attr('src');
        $('#magnify_glass').attr('src', '/static/music_streaming/img/search_magnifying_glass_icon_select.png');
        $('#magnify_glass').attr('alt-select', temp);
        $('h2.search_bar').removeClass('hover stable');
        $('h2.search_bar').addClass('select');
        $('#left_sidebar').removeClass('gradient');
        $('#left_sidebar').addClass('blackOut');
        var url = window.location.href;
        var usernameArr = url.split("/");
        var username = usernameArr[3];
        var search_url = "/"+username+"/search";
        width = ($(window).width()-218.5);
        height = ($(window).height()-78);
        height_recsearch = ($(window).height()-149);
        console.log(height_recsearch);
        $('#main_content').addClass('toSize');
        $('#main_content').width(width);
        $('#main_content').height(height);
        $('#recent_searches').height(height_recsearch);
        $.ajax({
            url: search_url,
            success: function(serverResponse) {
                console.log('success. serverResponse:', serverResponse)
                $('#main_content').prepend(serverResponse);
            }
        });
    });
    $('#your_music').click(function(){
        console.log('Your music tab was clicked!')
        $('h2.search_bar').removeClass('hover stable');
        $('h2.search_bar').addClass('select');
        $('#left_sidebar').addClass('blackOut');
        var url = window.location.href;
        var usernameArr = url.split("/");
        var username = usernameArr[3];
        var search_url = "/"+username+"/playlists";
        width = ($(window).width()-218.5);
        height = ($(window).height()-78);
        height_recsearch = ($(window).height()-149);
        $('#main_content').addClass('toSize');
        $('#main_content').addClass('gradient');
        $('#main_content').width(width);
        $('#main_content').height(height);
        $('#left_sidebar').height(height);
        $('#recent_searches').height(height_recsearch);
        $.ajax({
            url: search_url,
            success: function(serverResponse) {
                console.log('success. serverResponse:', serverResponse)
                $('#main_content').prepend(serverResponse);
            }
        });
    });
    $(window).resize(function(){
        width = ($(window).width()-218.5);
        height = ($(window).height()-78);
        console.log('height:',height,'width:',width)
        $('#main_content').width(width);
        $('#main_content').height(height);
        $('#left_sidebar').height(height);
    });
    $('h2').mouseenter(function(){
        if ($(this).not('.search_bar').hasClass('stable')){
            $(this).not('.search_bar').addClass('hover');
            $(this).mouseleave(function(){
            $(this).not('.search_bar').removeClass('hover');
            });
        };
    });
    $('h2').click(sideBarClickOff)
    $('.main_logo').click(function(){
        sideBarClickOff();
        $('#home').addClass('select');
        $('#home').removeClass('stable');
    });
});