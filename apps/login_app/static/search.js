$(document).ready(function(){
    $('#invitebox').keyup(function(){
        $.ajax({
            url: '/group/search',
            method: 'POST',
            data: $('#inviteform').serialize()
        })
        .done(function(res){
            $("#searchresults").html(res)
        })
        return false
    });
})
$(document).on('click', '.searchitem', function(){
    searchtext = $(this).html()
    $("#invitebox").val(searchtext)
    $('.searchitem').hide()
})
