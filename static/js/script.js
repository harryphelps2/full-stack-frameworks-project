$(document).ready(function(){

	$(".minus, .plus").click(function(e){
		var $button = $(this);
		var $quantity = $button.siblings(".quantity");
		var quantity = parseInt($quantity.text());

		if ($button.hasClass("minus")){
			quantity--;
		} else {
			quantity++;
		}
			$quantity.text(quantity);

		if (quantity == 1){
			$button.attr("disabled","disabled")
		} else {
			$button.siblings(".minus").attr("disabled",false)
        }
        $(".add-to-cart").attr({'value':quantity})
    });
    
})