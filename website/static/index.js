function deleteNote(noteId) {
    if (window.confirm("Proceeding will perminantly delete all content within the note and cannot be recovered. Proceed?")) {
        fetch("delete-note", {
            method: "POST",
            body: JSON.stringify({ noteId: noteId }),
        }).then((_res) => {
            window.location.href = "/";
})}}
