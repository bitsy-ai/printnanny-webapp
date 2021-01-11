AlertWebsocket = function(base_url){
    const WS_URL = `${base_url}/alerts/`;
    const ws = new WebSocket(WS_URL);
    ws.onmessage = (msg) => {
        console.log(msg)
    }
        ws.onopen = () => {
        console.log(`Connected to ${WS_URL}`);
    }
}