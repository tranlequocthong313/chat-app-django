'use strict';

import { getContentFromJSONElementById } from "./helper.js";

const receivedMsgSFX = "http://127.0.0.1:8000/static/media/received message sfx.mp3";
function playReceivedMsgSFX(msg) {
    if (msg.authorName === getContentFromJSONElementById("user-username")) {
        return;
    }
    var audio = new Audio(receivedMsgSFX);
    audio.play();
}

export default playReceivedMsgSFX;
