const roomID = getContentFromJSONElementById('room-id')
let url = `ws://${window.location.host}/ws/chat/${roomID}/`

const chatSocket = new WebSocket(url)

chatSocket.onmessage = function (e) {
    let data = JSON.parse(e.data)
    if (data.type == 'broadcast') {
        renderNewMessage(JSON.parse(data.message))
    }
}

let form = document.getElementById('message-box-form')
form.addEventListener('submit', e => {
    e.preventDefault()
    let content = e.target.message.value
    const authorID = getContentFromJSONElementById('user-id')
    const authorName = getContentFromJSONElementById('user-username')
    const authorAvatar = getContentFromJSONElementById('user-avatar')
    const roomID = getContentFromJSONElementById('room-id')
    const sendDate = new Date().toLocaleString()
    chatSocket.send(JSON.stringify({
        content, authorID, authorName, authorAvatar, roomID, sendDate
    }))
    form.reset()
})


let chatSection = document.getElementById('chat-section')
function renderNewMessage(msg) {
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

function getContentFromJSONElementById(id) {
    return JSON.parse(document.getElementById(id).textContent)
}


