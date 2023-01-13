chatSocket = null;

function connectToWebSocket() {
    chatSocket = new WebSocket(getWebSockURL())
    chatSocket.onmessage = receiveMessageFromServer
}

function getWebSockURL() {
    const roomID = getContentFromJSONElementById('room-id')
    return `ws://${window.location.host}/ws/chat/${roomID}/`
}

function receiveMessageFromServer(e) {
    let data = JSON.parse(e.data)
    if (data.type == 'broadcast') {
        renderNewMessageToHTML(JSON.parse(data.message))
    }
}

function renderNewMessageToHTML(msg) {
    let chatSection = document.getElementById('chat-section')
    if (msg.authorName == getContentFromJSONElementById('user-username')) {
        chatSection.insertAdjacentHTML('beforeend', `
        <li style="background-color: #f0f0f0; border-radius: 12px; margin: 12px 0;">
            <div class="d-flex align-items-center justify-content-center">
                <img style="width: 20px; height: 20px; border-radius: 50%;" src="${msg.authorAvatar}"
                    alt="${msg.authorName}">
                <p>${msg.authorName}</p>
                <p style="margin-left: 16px;">${msg.content}</p>
            </div>
        </li>
        `)
    } else {
        chatSection.insertAdjacentHTML('beforeend', `
        <li style="#f0f0f0; border-radius: 12px; margin: 12px 0;">
            <div class="d-flex align-items-center justify-content-center">
                <img style="width: 20px; height: 20px; border-radius: 50%;" src="${msg.authorAvatar}"
                    alt="${msg.authorName}">
                <p>${msg.authorName}</p>
                <p style="margin-left: 16px;">${msg.content}</p>
            </div>
        </li>
        `)
    }
}

const form = document.getElementById('message-box-form')
form.onsubmit = sendMessage

function sendMessage(e) {
    e.preventDefault()
    const content = e.target.message.value
    const authorID = getContentFromJSONElementById('user-id')
    const authorName = getContentFromJSONElementById('user-username')
    const authorAvatar = getContentFromJSONElementById('user-avatar')
    const roomID = getContentFromJSONElementById('room-id')
    chatSocket.send(JSON.stringify({
        content, authorID, authorName, authorAvatar, roomID
    }))
    form.reset()
}

function getContentFromJSONElementById(id) {
    return JSON.parse(document.getElementById(id).textContent)
}

connectToWebSocket()