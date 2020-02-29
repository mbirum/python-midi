let data = new Array();
for (let i = 0; i < 12; i++) {
    let note, noteSHA, velocity, velocitySHA = '';
    let url = `https://api.github.com/repos/mbirum/python-midi/contents/touch-pins/${i}/note`;
    $.get(url, function(response) {
        note = atob(response.content);
        noteSHA = response.sha;
        $(`#${i}note`).val(note);
        url = `https://api.github.com/repos/mbirum/python-midi/contents/touch-pins/${i}/velocity`;
        $.get(url, function(response) {
            velocity = atob(response.content);
            velocitySHA = response.sha;
            $(`#${i}vel`).val(velocity);
            data.push({note: {sha: noteSHA, value: note}, velocity: {sha: velocitySHA, value: velocity}});
        });
    });
}

function updateContent(i, type, callback) {
    let url = `https://api.github.com/repos/mbirum/python-midi/contents/touch-pins/${i}/${type}`;
    $.ajax({
        url: url, 
        type: 'PUT',
        headers: {
            Authorization: "token a4cc84266549210db944b975a320034977ed9753"
        },
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
    updateContent(i, 'note', function() {
        updateContent(i, 'velocity');
    });
    $(this).hide();
});

$("input").change(function(e) {
    let i = this.id.replace("note", "").replace("vel", "");
    if ($(this).hasClass('note')) {
        data[i].note.value = $(this).val();
    }
    else {
        data[i].velocity.value = $(this).val();
    }
    $(`#${i}sync`).show();
});