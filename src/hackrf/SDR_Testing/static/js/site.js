$(function() {
	getChecked()
	$('option').click(function() {
		getChecked()
	})
})

function getChecked() {
	var selects = $('.scan_group > select')
	var curr = '<div><h2 class="currently_selected">Currently Selected</h2></div>'
	$.each(selects, function() {
		var id = $(this).attr('id')
		var options = $(this).find("option:selected")
		var checked = new Array()
		$.each(options, function() {
			checked.push($(this).text())
		})
		var item = '<h4>' + id + '</h4><div>' + checked +'</div>'
		curr = curr+item
	})
	$('.currently_checked').html(curr)
}

function allList(id) {
	var new_id = "#" + id.replace('.', '\\\\.') + " option";
	$(new_id).prop("selected", true);
}
function clearList(id) {
	var new_id = "#" + id.replace('.', '\\\\.') + " option:selected";
	$(new_id).prop("selected", false);
}
