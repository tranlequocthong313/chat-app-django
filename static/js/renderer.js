import { getContentFromJSONElementById, scrollSmoothToBottomByID, getTimeSince } from "./helper.js";

const chatSectionID = 'chat-section'
const chatSection = document.getElementById(chatSectionID)

export function renderMessages(msgs) {
    console.log(msgs)
    msgs.forEach((msg, i) => {
        const isLastMessage = i == msgs.length - 1;
        insertMessageIntoHTML(msg);
        if (isLastMessage) {
            scrollSmoothToBottomByID(chatSectionID);
        }
    });
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
            <img class="userMsgAvatar" src="${msg.authorAvatar}"
                alt="${msg.authorName}">
            <div class="app-container">
                <b style="color: #000">${msg.authorName}</b>
                <p>${msg.content}</p>
                <span>${getTimeSince(msg.sendDate)} ago</span>
            </div>
        </div>
        `)
}