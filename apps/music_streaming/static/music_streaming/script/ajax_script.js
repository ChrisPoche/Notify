function sideBarClickOff(){
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
        temp = $('#magnify_glass').attr('src');
        $('#magnify_glass').attr('src', '/static/music_streaming/img/search_magnifying_glass_icon_select.png');
        $('#magnify_glass').attr('alt-select', temp);
        $('h2.search_bar').removeClass('hover stable');
        $('h2.search_bar').addClass('select');
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