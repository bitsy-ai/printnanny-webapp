AlertWebsocket = function(base_url){
    const WS_URL = `${base_url}/alerts/`;
    const ws = new WebSocket(WS_URL);

    self = this;

    const alertsBadge = $("#alerts-badge");
    const alertsContainer = $("#alerts-container");

    self.appendAlert = function(message){
        console.log(message)
        var data =  JSON.parse(message);
        console.log(data)
        alertsContainer.append(
            `<a href="${data.dashboard_url}" class="dropdown-item notify-item">
                <div class="notify-icon ${data.css_color_class}">
                    <i class=${data.css_icon_class}></i>
                </div>
                <p class="notify-details">${data.alert_subtype_display}
                    <small class="text-muted">${data.naturaltime}</small>
                </p>
            </a>`
        )

    }
    ws.onmessage = async (msg) => {
        alertsBadge.show()
        console.log(msg)
        self.appendAlert(await msg.data.text())
    }
        ws.onopen = () => {
        console.log(`Connected to ${WS_URL}`);
    }
}