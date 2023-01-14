import { connectToWebSocket, sendMessage } from "./socket.js";
import { getContentFromJSONElementById } from "./helper.js";
import { renderMessages } from "./renderer.js";

function app() {
    // Connect to web socket
    const roomID = getContentFromJSONElementById('room-id');
    const url = `ws://${window.location.host}/ws/chat/${roomID}/`;
    connectToWebSocket(url)

    // Render messages when user join to the room
    window.onload = renderMessages(getContentFromJSONElementById('messages'));

    // Send new message from the form to server
    const messageForm = document.getElementById('message-box-form');
    messageForm.onsubmit = e => {
        e.preventDefault()
        const data = {};
        data['content'] = e.target.message.value;
        data['authorID'] = getContentFromJSONElementById('user-id');
        data['authorName'] = getContentFromJSONElementById('user-username');
        data['authorAvatar'] = getContentFromJSONElementById('user-avatar');
        data['roomID'] = getContentFromJSONElementById('room-id');
        data['sendDate'] = new Date()
        sendMessage(data)
        messageForm.reset();
    }
}

app();