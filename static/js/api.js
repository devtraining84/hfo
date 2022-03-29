function show_id(event)
{
    console.log("najechałeś myszka na element")
    var type = this.dataset.type;
    var address = '/get_org_by_type';
    var data = {'type':type};
    console.log(type);
    $.get(address,data, function (data, status) {
        console.log("pobrałem dane:");
        console.log(data);
        $('.org').html(data);
        console.log("podmieniłem dane na stronie");
    });

   }







$( document ).ready(function() {
    var li_buttons = $('.org');
    //console.log(li_buttons)
    li_buttons.click(show_id);

});



