// Javascript can't get data from Django's views directly
// so it provides the JSON element feature and Javascript
// can get the data like get DOM elements.
export function getContentFromJSONElementById(id) {
    return JSON.parse(document.getElementById(id).textContent)
}

export function scrollSmoothToBottomByID(id, speed = 500) {
    const div = document.getElementById(id)
    $("#" + id).animate(
        {
            scrollTop: div.scrollHeight - div.clientHeight,
        },
        speed
    );
}

export function getTimeSince(date) {
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