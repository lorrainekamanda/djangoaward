$('#likes').click(function(){
    var ansid;
    ansid = $(this).attr("data-ansid");
            $.get('/questions/add_like/', {image_id: ansid}, function(data){
        $('#like_count').html(data);
    $('#likes').hide();
});
});