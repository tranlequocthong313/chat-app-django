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
    chatSection.insertAdjacentHTML('beforeend', `
        <li>
            <div style="display: flex; align-items: center; justify-content: center;">
                <img style="width: 20px; height: 20px; border-radius: 50%;" src="${msg.authorAvatar}"
                    alt="${msg.authorName}">
                <p style="margin-left: 16px;">${msg.content}</p>
            </div>
            <p>${msg.sendDate}</p>
        </li>
        `)
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
    const sendDate = new Date().toLocaleString()
    chatSocket.send(JSON.stringify({
        content, authorID, authorName, authorAvatar, roomID, sendDate
    }))
    form.reset()
}

function getContentFromJSONElementById(id) {
    return JSON.parse(document.getElementById(id).textContent)
}

connectToWebSocket()