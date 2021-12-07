// Stripe - Element
// Get the stripe public key
// And client secret from template using jQuery
//
// 1 Getting their ids and using the .text function.
// 2 Slice off first and last character which represent quotation marks.
// 3 Then using Stripe (js) provided function to store public key
// 4 And use it to create an instance of stripe elements
// 5 Using Stripe provided styling to apply on Stripe element
// 5 Adjusting some color and font settings
// 5 Matching uikit uk-text-danger color class
// 6 And create card element while using custom declared styles
// 7 Then mount the card element to the HTML id #card-element to use in template

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);  // 1
var clientSecret = $('#id_client_secret').text().slice(1, -1);  // 2
var stripe = Stripe(stripePublicKey);  // 3
var elements = stripe.elements();  // 4
// 5
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '14px',
        '::placeholder': {
            color: '#999'
        }
    },
    invalid: {
        color: '#f0506e',
        iconColor: '#f0506e'
    }
};
var card = elements.create('card', {style: style});  // 6
card.mount('#card-element');  // 7



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
//
// 1 Get form element
// 2 Add event listener on submit
// 3 Prevent default 'post' submission action
// 4 Disable card element
// 5 Disable submit button
// 6 Execute Stripe 'confirm card payment method' to send card info first
// 7 Then execute function based on result
// 8 If result or reply from Stripe is an error response
//   display error message under the card field
// 9 And re-enable card element
// 10 and submit button to allow user to fix issue
// 11 Otherwise if the response from Stripe is positive we submit the form

var form = document.getElementById('payment-form');  // 1
// 2
form.addEventListener('submit', function(ev) {
    ev.preventDefault();  // 3
    card.update({ 'disabled': true});  // 4
    $('#submit-button').attr('disabled', true);  // 5
    
    // 6
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    // 7
    }).then(function(result) {
        // 8
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span role="alert" uk-icon="icon: warning"></span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});  // 9
            $('#submit-button').attr('disabled', false);  // 10
        // 11
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});