// Get the stripe public key
// And client secret from template using jQuery

// Getting their ids and using the .text function.
// Slice off first and last character which represent quotation marks.
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);

// Then using Stripe (js) provided function to store public key
var stripe = Stripe(stripe_public_key);
// And use it to create an instance of stripe elements
var elements = stripe.elements();

// Using Stripe provided styling to apply on Stripe element
var style = {
    base: {
        // Adjusting some color and font settings
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '14px',
        '::placeholder': {
            color: '#999'
        }
    },
    invalid: {
        // Matching uikit uk-text-danger color class
        color: '#f0506e',
        iconColor: '#f0506e'
    }
};

// And create card element while using custom declared styles
var card = elements.create('card', {style: style});

// Then mount the card element to the HTML id #card-element to use in template
card.mount('#card-element');