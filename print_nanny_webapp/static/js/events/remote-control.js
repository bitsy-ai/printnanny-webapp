RemoteControlEventSubscription = function(base_url, device_id){
    const WS_URL = `${base_url}/${device_id}/remote-control/`;
    const ws = new WebSocket(WS_URL);
    ws.onmessage = (msg) => {
        console.log(msg)
    }
        ws.onopen = () => {
        console.log(`Connected to ${WS_URL}`);
    }
}