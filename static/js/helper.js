'use strict';

/**
 * Validate types more correctly than typeof
 * @param {*} value 
 * @returns type of the value with capitalizing first letter
 */
function typeOf(value) {
    return Object.prototype.toString.call(value).slice(8, -1);
}

// Javascript can't get data from Django's views directly
// so it provides the JSON element feature and Javascript
// can get the data like get DOM elements.
function getContentFromJSONElementById(id) {
    return JSON.parse(document.getElementById(id).textContent);
}

function scrollSmoothToBottomByID(id, speed = 500) {
    const div = document.getElementById(id);
    $("#" + id).animate(
        {
            scrollTop: div.scrollHeight - div.clientHeight,
        },
        speed
    );
}

function getTimeSince(date) {
    var seconds = Math.floor((new Date() - new Date(date)) / 1000);

    var interval = seconds / 31536000;

    if (interval > 1) {
        return Math.floor(interval) + " years";
    }
    interval = seconds / 2592000;
    if (interval > 1) {
        return Math.floor(interval) + " months";
    }
    interval = seconds / 86400;
    if (interval > 1) {
        return Math.floor(interval) + " days";
    }
    interval = seconds / 3600;
    if (interval > 1) {
        return Math.floor(interval) + " hours";
    }
    interval = seconds / 60;
    if (interval > 1) {
        return Math.floor(interval) + " minutes";
    }
    return Math.floor(seconds) + " seconds";
}

export { getContentFromJSONElementById, getTimeSince, scrollSmoothToBottomByID };
