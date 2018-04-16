/*
#
# SUPERFREQ socket.io library
# Copyright (C) 2018 Team SUPERFREQ, CU Boulder ITP <itp@colorado.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
*/

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
