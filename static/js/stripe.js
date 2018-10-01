// Custom styling can be passed to options when creating an Element.
var stripe = Stripe('pk_test_oGzjqmtiyqFycxaJ7nO1aTgL');
var elements = stripe.elements()
var style = {
    base: {
      // Add your base input styles here. For example:
      fontSize: '16px',
      color: "#32325d",
    }
  };
  
  // Create an instance of the card Element.
var card = elements.create('card', {style: style});
  
  // Add an instance of the card Element into the `card-element` <div>.
  card.mount('#card-element');

  card.addEventListener('change', function(event) {
    var displayError = document.getElementById('card-errors');
    if (event.error) {
      displayError.textContent = event.error.message;
    } else {
      displayError.textContent = '';
    }
  });

// Create a token or display an error when the form is submitted.
var form = document.getElementById('payment-form');
form.addEventListener('submit', function(event) {
  event.preventDefault();

  stripe.createToken(card).then(function(result) {
    if (result.error) {
      // Inform the customer that there was an error.
      var errorElement = document.getElementById('card-errors');
      errorElement.textContent = result.error.message;
    } else {
      // Send the token to your server.
      stripeTokenHandler(result.token);
    }
  });
});

function stripeTokenHandler(token) {
    // Insert the token ID into the form so it gets submitted to the server
    var form = document.getElementById('payment-form');
    var hiddenInput = document.createElement('input');
    hiddenInput.setAttribute('type', 'hidden');
    hiddenInput.setAttribute('name', 'stripeToken');
    hiddenInput.setAttribute('value', token.id);
    form.appendChild(hiddenInput);
  
    // Submit the form
    form.submit();
  }
// $(function(){
//     $("#payment-form").submit(function(){
//         var form = this;
//         var card = {
//             number: $("#credit-card-number").val(),
//             expMonth: $("#id_expiry_month").val(),
//             expYear: $("#id_expiry_year").val(),
//             cvc: $("#id_cvv").val(),
//         };
    
//     Stripe.createToken(card).then(function(status, response) {
//         if (status === 200) {
//             $("#credit-card-errors").hide();
//             $("#id_stripe_id").val(response.id);

//             $("#id_credit_card_number").removeAttr('name');
//             $("#id_cvv").removeAttr('name');
//             $("#id_expiry_month").removeAttr('name');
//             $("#id_expiry_year").removeAttr('name');

//             form.submit();
//         } else {
//             $("#stripe-error-message").text(response.error.message);
//             $("#credit-card-errors").show()
//             $("#validate_card_btn").attr("disabled", false);
//         }
//     });
//     return false
//     })
// })