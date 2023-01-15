let chatSocket = null
let url = `ws://${window.location.host}/ws/chat/`;

export function connectToWebSocket(roomID) {
    chatSocket = new WebSocket(url + roomID)
    return chatSocket
}

export function sendMessage(data) {
    chatSocket.send(JSON.stringify(data))
}