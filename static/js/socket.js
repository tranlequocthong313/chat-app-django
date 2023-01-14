import { renderMessages } from "./renderer.js";

let chatSocket = null

export function connectToWebSocket(url) {
    chatSocket = new WebSocket(url)
    chatSocket.onmessage = receiveMessageFromServer
}

function receiveMessageFromServer(e) {
    let data = JSON.parse(e.data)
    if (data.type == 'broadcast') {
        renderMessages([JSON.parse(data.message)])
    }
}

export function sendMessage(data) {
    chatSocket.send(JSON.stringify(data))
}