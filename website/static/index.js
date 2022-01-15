function postJson(url, json, options) {
    options = options || {}
    let params = {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(json)
    }
    Object.assign(params, options);
    return fetch(url, params);
}

function deleteNote(noteId) {
    if (window.confirm("Proceeding will perminantly delete all content within the note and cannot be recovered. Proceed?")) {
        postJson("delete-note", { noteId: noteId }).then((_res) => {
            window.location.href = "/";
    })
}}

function shareNote(noteId, userId) {
    let user = window.prompt("Enter the username of the person you would like to share this note with", "");
    let text;
    if (user == null || user == "") {
        text = "note sharing canceled";
    }
    else {
        postJson("share-note", { noteId: noteId, username: user }).then((response) => {
            return response.json();
        }).then((data) => {
            if(data.result) {
                window.location.href = window.location.href;
            } else {
                alert(`Error sharing: ${data.message || 'Unknown error, please contact support'}`)
            }
        })
    }
}

function editNote(noteId) {
    let edit = window.prompt("editing current note", "");
    postJson("edit-note", { noteId: noteId }).then((response) => {
        return response.json();
    }).then((data) => {
        if(data.result) {
            window.location.href = window.location.href;
        } else {
            alert(`Error editing: ${data.message || 'Unknown error, please contact support'}`)
        }
    })
}
