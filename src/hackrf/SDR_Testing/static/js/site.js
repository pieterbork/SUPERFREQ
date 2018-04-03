$(function() {
	getChecked()
	$('option').click(function() {
		getChecked()
	})
	$('#scan_name').on('input', function() {
		var input = $(this).val().toLowerCase()
		if(input.indexOf("carlos") >= 0) window.location = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
	})
})

function getChecked() {
	var selects = $('.scan_group > select')
	var curr = '<div><h2 class="currently_selected">Currently Selected</h2></div>'
	var total_checked = 0
	var any_checked = false
	$.each(selects, function() {
		var id = $(this).prev().text()
		var options = $(this).find("option:selected")
		var checked = new Array()
		$.each(options, function() {
			any_checked = true
			checked.push($(this).text())
			total_checked += 1
		})
		var item = '<h4>' + id + '</h4><div>' + checked +'</div>'
		if(checked.length > 0) curr = curr+item
	})
	var scantime = $('#scan_time').val()
	if(total_checked > 0 && scantime >0) {
		curr += '<div>Total # of channels: ' + total_checked + '</div>' 
		var time_per_chan = Math.round((scantime/total_checked))
		curr += '<div>Scan time per channel: ' + time_per_chan + ' seconds</div>'
	}

	if(!any_checked) curr = ""

	$('.currently_checked').html(curr)
}

function allList(id) {
	var new_id = "#" + id.replace('.', '\\\\.') + " option";
	$(new_id).prop("selected", true);
	getChecked()
}
function clearList(id) {
	var new_id = "#" + id.replace('.', '\\\\.') + " option:selected";
	$(new_id).prop("selected", false);
	getChecked()
}
