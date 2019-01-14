function checkInventoryValidation(inputElement) {
    var $this = $(inputElement);
    var $form = $this.closest('form');
    // setting the url for the validation view
    // this can be anything different according to the
    // url structure of the product
    var url = '/verify-form/' + window.location.pathname.split('/')[1] + '/?value=' + $this.val();
    $form.find('[type=submit]').addClass('loading').prop('disabled', true);
    return $.ajax({
        type: "get",
        url: url,
        success: function (response) {
            $form.find('[type=submit]').removeClass('loading');
            // select the modal which displays error
            $errorModal = $('#error_modal')
            if (response.message === 'ok') {
                // input is valid, empty the error modal
                $errorModal.find('.modal-body').html('');
                // enable the submit button
                $form.find('[type=submit]').prop('disabled', false);
            } else if (response.message === 'error') {
                // input is invalid, put the error message from server into error modal
                // do not enable the submit button
                $errorModal.find('.modal-body').html(
                    '<p class="warning">' + response.error + '</p>'
                );
                // show the modal with error
                $errorModal.modal('show');
            }
        }
    });
}

$(function () {
    // check for existing quantity fields in ajax_validation forms
    var $validateInputsInit = $('.ajax_validation').find('#id_quantity');
    // if they exist, validate them on page load
    if ($validateInputsInit.length) {
        $validateInputsInit.each(function (index, element) {
            checkInventoryValidation(this);
        });
    }

    // listen for changes on quantity fields in ajax_validation forms
    $('.ajax_validation').on('change', '#id_quantity', function () {
        checkInventoryValidation(this);
    });

    // validate quantity fields in ajax_validation forms, when the user submits the form
    // this way if the stock changed between the users selection and form submission,
    // they will be notified again
    $('.ajax_validation').on('submit', function (e) {
        // prevent default submit of form
        e.preventDefault();
        var $form = (this);
        // get all the input fields to be validated
        var $validateInputs = $(this).find('#id_quantity');
        if ($validateInputs.length) {
            var validated = 0;
            var valid = true;
            $validateInputs.each(function (index, element) {
                // validate the input
                checkInventoryValidation(this).done(function (response) {
                    validated += 1;
                    // if input is not valid, mark the flag as false
                    if (response.message !== "ok") {
                        valid = false;
                    }
                    // if all the response for all the inputs arrived and none are invalid,
                    // submit the form normally
                    if (valid && validated == $validateInputs.length) {
                        $form.submit();
                    }
                });
            });
        }
    });
});