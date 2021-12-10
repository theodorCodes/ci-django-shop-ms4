// Stripe - Element
// Get the stripe public key
// And client secret from template using jQuery

// Getting their ids and using the .text function.
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
// Slice off first and last character which represent quotation marks.
var clientSecret = $('#id_client_secret').text().slice(1, -1);
// Then using Stripe (js) provided function to store public key
var stripe = Stripe(stripePublicKey);
// And use it to create an instance of stripe elements
var elements = stripe.elements();

// Using Stripe provided styling to apply on Stripe element
var style = {
    // Adjusting some color and font settings
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '14px',
        '::placeholder': {
            color: '#999'
        }
    },
    // Matching uikit uk-text-danger color class
    invalid: {
        color: '#f0506e',
        iconColor: '#f0506e'
    }
};

// And create card element while using custom declared styles
var card = elements.create('card', {style: style});
// Then mount the card element to the HTML id #card-element to use in template
card.mount('#card-element');



// Stripe - Event Listener on 'card'
// Handle realtime validation errors on the card element
//
// Adding listener on the card element
// Checking if any errors
// If error, display error message under the card field

card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span role="alert" uk-icon="icon: warning"></span>
            <span class="uk-text-small">${event.error.message}</span>`;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});



// Stripe - Submit Event Listener on 'form'

// Get form element
var form = document.getElementById('payment-form');
// Add event listener on submit
form.addEventListener('submit', function(ev) {
    ev.preventDefault();  // Prevent default 'post' submission action
    card.update({ 'disabled': true});  // Disable card element
    $('#submit-button').attr('disabled', true);  // Disable submit button
    $('#payment-form').fadeToggle(100);  // Loading spinner
    $('#loading-overlay').fadeToggle(100);  // Loading spinner

    // Save saved_info boolean value
    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    // Save {% csrf_token %} from the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    // Create object with the above info to pass to new view
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    // Save new url, cache_checkout_data function in views.py
    var url = '/checkout/cache_checkout_data/';

    // Then posting postData to new view using $.jQuery
    // But only if payment intent was conirmed and updated before, using .done
    // and call-back function
    $.post(url, postData).done(function () {
        // Executing .confirmCardPayment method in the call-back function
        // with required payment intent info that is saved in var form above
        // using $.trim to strip off whitespace
        stripe.confirmCardPayment(clientSecret, {
            // Indicating payment info
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address:{
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        // postal code provided by card element
                        state: $.trim(form.county.value),
                    }
                }
            },
            // Indicating shipping info
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.postcode.value),
                    state: $.trim(form.county.value),
                }
            },
        // Then execute function based on result
        }).then(function(result) {
            // If result or reply from Stripe is an error response
            // display error message under the card field
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span role="alert" uk-icon="icon: warning"></span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $('#payment-form').fadeToggle(100);  // Loading spinner
                $('#loading-overlay').fadeToggle(100);  // Loading spinner
                // And re-enable card element
                card.update({ 'disabled': false});
                // and submit button to allow user to fix issue
                $('#submit-button').attr('disabled', false);
            // Otherwise if the response from Stripe is positive we submit the form
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    // Failure function will be triggered if bad view response 400
    }).fail(function () {
        // Reloading the page, and the error will be in django messages
        location.reload();
    })
});
