var socket;
$("body").css("overflow", "hidden");
$(document).ready(function() {
	socket = io.connect("http://" + document.domain + ":" + location.port);
	socket.on('update', function(data) {
		if (data.msg == "Done") {
			$('#scan_status').first().html("<h2>Done</h2>");
			$('#results_link').first().css("bottom", "0px");
			$('#ring_container').first().css("opacity", "0");
			$('#status').first().css("background", "#55bb55");
		} else {
			$('#scan_status')[0].innerHTML = data.msg;
		}
	});
	socket.on('wifi_count', function(data) {
		$('#wifi_packet_count')[0].innerHTML = data.msg;
	});
	socket.on('zigbee_count', function(data) {
		$('#zigbee_packet_count')[0].innerHTML = data.msg;
	});
	socket.on('bt_count', function(data) {
		$('#bt_packet_count')[0].innerHTML = data.msg;
	});
	socket.on('progress', function(data) {
		if (!isNaN(data.msg)) {
			var percent = Math.round(Number(data.msg) / total_scan_time * 100);
			if (percent >= 0 && percent <= 100) {
				$('#progress_percent')[0].innerHTML = percent;
				if (percent >= 99) {
					percent += 1;
				}
				$('#progress_bar')[0].style.width = String(percent) + "%";
			}
		}
	});
});
