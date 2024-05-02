$(function () {
    let element = $('#toggle_header');
    element.addClass('red')
    element.click(function () { 
        if (element.hasClass('red')) { 
            element.removeClass('red');
            element.addClass('green');
        } else if (element.hasClass('green')) { 
            element.removeClass('green');
            element.addClass('red');
        }
    });
});
