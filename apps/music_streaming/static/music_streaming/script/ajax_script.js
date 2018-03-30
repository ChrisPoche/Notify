// function run when Search, Home or Your Music are clicked on left sidebar, resets the sidebar color and returns text back to stable (gray) class
function sideBarClickOff(){
    $('#main_content').html('');
    if($('#left_sidebar').attr('class') == 'blackOut'){
        $('#left_sidebar').removeClass('blackOut');
        $('#left_sidebar').addClass('gradient');
    };
    $('h2').not('.search_bar').removeClass('hover select');
    $('h2').not(this).addClass('stable');
    $(this).removeClass('hover stable');
    $(this).not('.search_bar').addClass('select');
    $('#magnify_glass').attr('src', '/static/music_streaming/img/search_magnifying_glass_icon.png');
    $('#magnify_glass').attr('alt-hover', '/static/music_streaming/img/search_magnifying_glass_icon_hover.png');
    $('h2.search_bar').addClass('stable');
    $('h2.search_bar').removeClass('select');
    return;
};
$(document).ready(function(){
    width = ($(window).width()-218.5);
    height = ($(window).height()-78);
    $('#main_content').addClass('toSize');
    $('#main_content').width(width);
    $('#main_content').height(height);
    $('#left_sidebar').height(height);
    $(window).resize(function(){
        width = ($(window).width()-218.5);
        height = ($(window).height()-78);
        console.log('height:',height,'width:',width)
        $('#main_content').width(width);
        $('#main_content').height(height);
        $('#left_sidebar').height(height);
    });
    // If Sidebar - Search + Magnify Glass Icon is gray, hover over adds class that makes elements white and changes cursor to pointer
    $('.search').mouseenter(function(){
        if ($('.search_bar').hasClass('stable')){
            var temp = $('#magnify_glass').attr('src');
            $('#magnify_glass').attr('src', $('#magnify_glass').attr('alt-hover'));
            $('#magnify_glass').attr('alt-hover', temp);
            $('h2.search_bar').addClass('hover');
            
        };
    });
    // Hover off Sidebar - Search + Magnify Glass Icon restores stable (gray) class
    $('.search').mouseleave(function(){
        if ($('.search_bar').hasClass('hover')){
            var temp = $('#magnify_glass').attr('src');
            $('#magnify_glass').attr('src', $('#magnify_glass').attr('alt-hover'));
            $('#magnify_glass').attr('alt-hover', temp);
            $('h2.search_bar').removeClass('hover');
            
        }
    });
    // AJAX call to search page, changes Search + Magnify Glass Icon to green, slices username var from url to include in AJAX response
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
        height_recsearch = ($(window).height());
        console.log(height_recsearch);
        $('#main_content').addClass('toSize');
        $('#main_content').width(width);
        $('#main_content').height(height);
        $('#recent_searches').height(height);
        $.ajax({
            url: search_url,
            success: function(serverResponse) {
                console.log('success. serverResponse:', serverResponse)
                $('#main_content').prepend(serverResponse);
            }
        });
    });
    // AJAX call to your music page
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
        $('#main_content').addClass('toSize');
        
        $('#main_content').width(width);
        $('#main_content').height(height);
        $('#left_sidebar').height(height);
        $.ajax({
            url: search_url,
            success: function(serverResponse) {
                console.log('success. serverResponse:', serverResponse)
                $('#main_content').prepend(serverResponse);
            }
        });
    });
    // Hover over to highlight Home or Music in white, but NOT Search on left sidebar
    $('#main_content').click(function(){
        console.log('Your music tab was clicked!')
        $('h2.track').removeClass('hover stable');
        $('h2.track').addClass('select');
        width = ($(window).width()-218.5);
        widthfull = ($(window).width());
        height = ($(window).height()-78);
        $('#main_content').addClass('toSize');
        $('#main_content').width(width);
        $('#main_content').height(height);
        $('#media_player').width(widthfull);
        $.ajax({
            url: search_url,
            success: function(serverResponse) {
                console.log('success. serverResponse:', serverResponse)
                $('#media_player').html(serverResponse);
            }
        });
    });
    $('h2').mouseenter(function(){
        if ($(this).not('.search_bar').hasClass('stable')){
            $(this).not('.search_bar').addClass('hover');
            $(this).mouseleave(function(){
            $(this).not('.search_bar').removeClass('hover');
            });
        };
    });
    // Listener for sidebar tab change, function called on ln 2 ^
    $('h2').click(sideBarClickOff)
    // Click on logo or home tab to return home and reset sidebar tabs
    $('.main_logo').click(function(){
        sideBarClickOff();
        $('#home').addClass('select');
        $('#home').removeClass('stable');
        var url = window.location.href;
        var usernameArr = url.split("/");
        var username = usernameArr[3];
        var search_url = "/"+username+"/home";
        width = ($(window).width()-218.5);
        height = ($(window).height()-78);
        $.ajax({
            url: search_url,
            success: function(serverResponse) {
                console.log('success. serverResponse:', serverResponse)
                $('#main_content').html(serverResponse);
            }
        });
    });
    $('#home').click(function(){
        sideBarClickOff();
        $('#home').addClass('select');
        $('#home').removeClass('stable');
        var url = window.location.href;
        var usernameArr = url.split("/");
        var username = usernameArr[3];
        var search_url = "/"+username+"/home";
        width = ($(window).width()-218.5);
        height = ($(window).height()-78);
        $.ajax({
            url: search_url,
            success: function(serverResponse) {
                console.log('success. serverResponse:', serverResponse)
                $('#main_content').html(serverResponse);
            }
        });
    });
    
});