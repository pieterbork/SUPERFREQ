$(function() {
	getChecked()
	$('option').click(function() {
		getChecked()
	})
	$('#scan_name').on('input', function() {
		var input = $(this).val().toLowerCase()
		if(input.indexOf("carlos") >= 0) window.location = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
	})
	$('option').mousedown(function(e) {	//Changes the default action of clicking options to ctrl-click 
		e.preventDefault()
		$(this).prop('selected', $(this).prop('selected')? false:true)
	})
	$(document).keypress(function(e) {
		console.log("Keypress")
		if (e.which == 13) {
			submitScan()
		}
	})
})

function submitScan() {
	$("#scan_form_container").fadeTo("slow", 0)
	setTimeout(function() {
		$("#scan_form").submit()
	}, 550)
	$("#scan_form_container").fadeTo("slow", 1)
}

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
		if(checked.length > 0) {
			curr = curr + '<h4>' + id + '</h4><div>' + checked +'</div>'
		} else {
			curr = curr + '<h4>' + id + '</h4><div>None</div>'
		}
	})
	var scantime = $('#scan_time').val()
	if(total_checked > 0 && scantime >0) {
		curr += '<div>Total # of channels: ' + total_checked + '</div>' 
		var time_per_chan = Math.round((scantime/total_checked))
		curr += '<div>Scan time per channel: ' 
		if(scantime/total_checked < 0.75) curr += '< '
		curr += time_per_chan + ' second'
		if(!(time_per_chan == 1)) curr += 's'
		curr += '</div>'
	}

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
