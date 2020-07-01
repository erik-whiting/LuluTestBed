let track_list;

function load_function(band_object) {
    band_object = decodeHtmlCharCodes(band_object);
    track_list = JSON.parse(band_object);
}

function decodeHtmlCharCodes(str) {
  return str.replace(/(&#(\d+);)/g, function(match, capture, charCode) {
    return String.fromCharCode(charCode);
  });
}

function populate_table(track_list) {
    let albums = Object.keys(track_list);
    albums.forEach((album) =>{
        let htmlString = '';
        htmlString += '<ul>';
        track_list[album].forEach((song) => {
            let id = song['id'];
            let songName = song['songname'];
            htmlString += `<li id='song-${id}'>${songName}</li>`
        });
        htmlString += '</ul>';
        let band_table = document.getElementById('band-table');
        let row = band_table.insertRow(album);
        let album_cell = row.insertCell(0);
        album_cell.innerHTML = `<b>${album}</b>`;
        let cell = row.insertCell(1);
        cell.setAttribute('class', 'song-list')
        row.setAttribute('id', album);
        cell.innerHTML = htmlString
    });
}