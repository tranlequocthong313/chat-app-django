'use strict';

import { connectToWebSocket, sendMessage } from "./socket.js";
import { getContentFromJSONElementById } from "./helper.js";
import renderMessages from "./renderer.js";
import playReceivedMsgSFX from "./audio.js";

function initApp() {
    const roomID = getContentFromJSONElementById('room-id');
    var socket = connectToWebSocket(roomID);

    // Receive message from server
    socket.onmessage = receiveMessageFromServer;

    // Render messages when user joins to the room
    window.onload = renderMessages(getContentFromJSONElementById('messages'));

    // Send new message from the form's input to server
    const messageForm = document.getElementById('message-box-form');
    messageForm.onsubmit = (e) => {
        sendMessageToServer(e);
        messageForm.reset();
    };
};

function receiveMessageFromServer(e) {
    let data = JSON.parse(e.data);
    if (data.type === "broadcast") {
        handleNewMessage(data.message);
    }
};

function handleNewMessage(message) {
    const msg = JSON.parse(message);
    renderMessages([msg]);
    playReceivedMsgSFX(msg);
}

function sendMessageToServer(e) {
    e.preventDefault();
    const data = {};
    data['content'] = e.target.message.value;
    data['authorID'] = getContentFromJSONElementById('user-id');
    data['authorName'] = getContentFromJSONElementById('user-username');
    data['authorAvatar'] = getContentFromJSONElementById('user-avatar');
    data['roomID'] = getContentFromJSONElementById('room-id');
    data['sendDate'] = new Date();
    sendMessage(data);
};

document.addEventListener('DOMContentLoaded', initApp);
