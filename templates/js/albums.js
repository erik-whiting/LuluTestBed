let albums;

function load_function(albums_object) {
    albums_object = decodeHtmlCharCodes(albums_object);
    albums = JSON.parse(albums_object)
}

function decodeHtmlCharCodes(str) {
  return str.replace(/(&#(\d+);)/g, function(match, capture, charCode) {
    return String.fromCharCode(charCode);
  });
}

function populate_table(albums) {
    let album_table = document.getElementById('albums-table');
    let headers = album_table.insertRow(0);
    headers.insertCell(0).innerHTML = 'Album';
    headers.insertCell(1).innerHTML = 'Band';
    headers.insertCell(2).innerHTML = 'Songs';

    albums.forEach((album) => {
       let album_name_html = `<b>${album['albumname']}</b>`;
       let artist_url = `/bands/${album['bandid']}`;
       let artist_name_html = `<a href="${artist_url}"><i>${album['artist']}</i></a>`;
       let songs_html = '<ul>';
       album['songs'].forEach((song) => {
          songs_html += `<li>${song['songname']}</li>`;
       });
       songs_html += '</ul>';

       let row = album_table.insertRow(1);
       let album_cell = row.insertCell(0);
       let artist_cell = row.insertCell(1);
       let song_cell = row.insertCell(2);

       album_cell.innerHTML = album_name_html;
       artist_cell.innerHTML = artist_name_html;
       song_cell.setAttribute('class', 'song-list');
       song_cell.innerHTML = songs_html;
    });
}