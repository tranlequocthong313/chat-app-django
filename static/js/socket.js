'use strict';

let chatSocket = null;
let url = `ws://${window.location.host}/ws/chat/`;

function connectToWebSocket(roomID) {
    chatSocket = new WebSocket(url + roomID);
    return chatSocket;
}

function sendMessage(data) {
    chatSocket.send(JSON.stringify(data));
}

export {
    connectToWebSocket,
    sendMessage
};
