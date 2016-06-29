(function (window) {
	$(document).ready(main);

	function main() {
		var sock = new window.WebSocket('ws://192.168.1.179:8080');
		sock.onmessage = function(message) {
			var chat = $("#chat");
			try {
				var parts = JSON.parse(message.data);
				parts.forEach(function(value) {
					chat.append($("<li></li>").html(value));
				});
			} catch (e) {
				console.log("Your message is malformed:" + message.data);
			}
		};
		sock.onerror = function(error) {
			console.log("I'm angry:" + error);
		};
		$("#message").bind("keypress", function(e) {
			if (e.keyCode === 13) {
				sock.send($("#message").val());
			} else {
				console.log(e)
			}
		});
	}
})(window);
