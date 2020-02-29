let data = new Array();
for (let i = 0; i < 12; i++) {
    let note, noteSHA, velocity, velocitySHA = '';
    $.ajax({
        url: `https://api.github.com/repos/mbirum/python-midi/contents/touch-pins/${i}/note`,
        type: 'GET',
        headers: {Authorization: `token ${token.value}`},
        success: function(response) {
            note = atob(response.content);
            noteSHA = response.sha;
            $(`#${i}note`).val(note);

            $.ajax({
                url: `https://api.github.com/repos/mbirum/python-midi/contents/touch-pins/${i}/velocity`,
                type: 'GET',
                headers: {Authorization: `token ${token.value}`},
                success: function(response) {
                    velocity = atob(response.content);
                    velocitySHA = response.sha;
                    $(`#${i}vel`).val(velocity);
                    data.push({note: {sha: noteSHA, value: note}, velocity: {sha: velocitySHA, value: velocity}});
                }
            });
        }
    });
}

function updateContent(i, type, callback) {
    let url = `https://api.github.com/repos/mbirum/python-midi/contents/touch-pins/${i}/${type}`;
    $.ajax({
        url: url, 
        type: 'PUT',
        headers: {Authorization: `token ${token.value}`},
        contentType: "application/json",
        data: JSON.stringify({
            message: `app update ${i} ${type}`,
            content: btoa(data[i][type].value),
            sha: data[i][type].sha,
            committer: {
                name: 'Matt Birum',
                email: 'birum18@gmail.com'
            }
        }),
        success: callback
    });
}

$("button").click(function(e) {
    let i = this.id.replace("sync", "");
    if (data[i].note.value != $(`#${i}note`).val()) {
        data[i].note.value = $(`#${i}note`).val();
        updateContent(i, 'note', function(response) {
            data[i].note.sha = response.content.sha;
        });
    }
    if (data[i].velocity.value != $(`#${i}vel`).val()) {
        data[i].velocity.value = $(`#${i}vel`).val();
        updateContent(i, 'velocity', function(response) {
            data[i].velocity.sha = response.content.sha;
        });
    }
    
    $(this).hide();
});

$("input").change(function(e) {
    let i = this.id.replace("note", "").replace("vel", "");
    $(`#${i}sync`).show();
});