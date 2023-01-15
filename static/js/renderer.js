import { getContentFromJSONElementById, scrollSmoothToBottomByID, getTimeSince } from "./helper.js";

const chatSectionID = 'chat-section'
const chatSection = document.getElementById(chatSectionID)

export function renderMessages(msgs) {
    for (let i = 0; i < msgs.length; i++) {
        const isLastMessage = i == msgs.length - 1;
        insertMessageIntoHTML(msgs[i]);
        if (isLastMessage) {
            scrollSmoothToBottomByID(chatSectionID);
        }
    }
}

function insertMessageIntoHTML(msg) {
    const content = getBubbleChatBoxStyleByMessageOwner(msg)
    chatSection.innerHTML += content
}

function getBubbleChatBoxStyleByMessageOwner(msg) {
    return (msg.authorName === getContentFromJSONElementById('user-username')
        ? `<div class="d-flex align-items-center">
            <div class="app-container darker right">
                <p>${msg.content}</p>
                <span>${getTimeSince(msg.sendDate)} ago</span>
            </div>
        </div>`
        : `<div class="d-flex align-items-center">
            <img style="width: 20px; height: 20px; border-radius: 50%; margin-right: 8px;" src="${msg.authorAvatar}"
                alt="${msg.authorName}">
            <div class="app-container">
                <b style="color: #000">${msg.authorName}</b>
                <p>${msg.content}</p>
                <span>${getTimeSince(msg.sendDate)} ago</span>
            </div>
        </div>
        `)
}