(function ($) {

    $.contactVerification = function(options) {
        var settings = $.extend({
            sendButtonSelector: "#id_contact_button",
            confirmButtonSelector: "#id_confirm_button",
            onSendSuccess: null,
            onSendFail: null,
            onConfirmSuccess: null,
            onConfirmFail: null,
            countrySelector: null,
            contactSelector: "#id_contact",
            codeSelector: "#id_code"
        }, options );

        var $send_button = $(settings.sendButtonSelector);
        var $confirm_button = $(settings.confirmButtonSelector);
        var $input_country = $(settings.countrySelector);

        $.ajax({url: '/contact_verification/countries/'})
            .done(function(data) {
                $.each(data, function( index, value ) {
                    $input_country.append("<option value='" + value.number + "'>"+ value.name +"</option>")
                });
            });

        $send_button.click(function(){
            var country = $(settings.countrySelector).val();
            var contact = $(settings.contactSelector).val();

            $.ajax({
                url: '/contact_verification/pins/',
                method: 'post',
                data: {
                    country_number : country,
                    phone_number: contact
                }
            }).done(function(data) {
                if (settings.onSendSuccess){
                    settings.onSendSuccess(data);
                }
                else{
                    alert(data.message);
                }
            }).fail(function(data) {
                var message = "";
                $.each(data.responseJSON, function( key, value ) {
                    message += value + "\n";
                });
                alert(message);
            })
        });

        $confirm_button.click(function(){
            var country = $(settings.countrySelector).val();
            var contact = $(settings.contactSelector).val();
            var code = $(settings.codeSelector).val();

            $.ajax({
                url: '/contact_verification/contacts/',
                method: 'post',
                data: {
                    country_number : country,
                    phone_number: contact,
                    code: code
                }
            }).done(function(data) {
                if (settings.onConfirmSuccess){
                    settings.onConfirmSuccess(data);
                }
                else{
                    location.reload(true);
                }
            }).fail(function(data) {
                var message = "";
                $.each(data.responseJSON, function( key, value ) {
                    message += value + "\n";
                });
                alert(message);
            })
        });
    };
}( jQuery ));
