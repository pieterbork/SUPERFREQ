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
	var scantime = $('#scan_time').val()
	var total_checked = 0
	$.each(selects, function() {
		var name = $(this).attr('id')
		var id = $(this).prev().text()
		var options = $(this).find("option:selected")
		var checked = new Array()
		$.each(options, function() {
			checked.push($(this).text())
			total_checked += 1
		})
		if(checked.length > 0) {
			$(".checked_"+name).html(checked.join())
		} else {
			$(".checked_"+name).html("None")
		}
	})
	var time_per_chan = scantime/total_checked
	var units = "s"
	var prefix = ""
	if(time_per_chan < 0.75) prefix = " < "
	var tot_count = prefix + Math.round(time_per_chan) + units

	$('.tot_count').html(total_checked)
	$('.time_per_chan').html(tot_count)
}

/* Does nothing yet, but eventually when given [1,2,3,4,8,9] will return "1-4,8,9"*/
function getRanges(arr) {
	var i = 0
	var all_arrs = Array()
	while(i < arr.length) {
		var item = arr[i]
		var curr_arr = Array()
		curr_arr.push(item)
		i++
		if(i == arr.length) all_arrs.push(curr_arr)
		for(var j=i; j<arr.length; j++) {
			var ele = arr[j]
			i = j
			if(item == ele-1) {
				curr_arr.push(ele)
				item = ele
			}
			else {
				all_arrs.push(curr_arr)	
				break
			}
			if(j == arr.length-1) all_arrs.push(curr_arr)
		}
	}
	var out_arr = Array()
	$.each(all_arrs, function() {
		var len = this.length
		if(len <= 2) {
			var str = this.join()
			if(!out_arr.indexOf(str)) out_arr.push(str)
		}
		else out_arr.push(arr[0] + "-" + arr[len-1])
	})
	return out_arr.join()
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
