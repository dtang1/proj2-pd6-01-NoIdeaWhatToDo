
// code that removes non digits from the price input
$(function() {
	$("#price").on("input", function() {
		$(this).val($(this).val().replace(/\D/g,""));
	});
});




