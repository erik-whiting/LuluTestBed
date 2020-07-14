let bands;

function load_function(bands_object) {
    bands_object = decodeHtmlCharCodes(bands_object);
    bands = JSON.parse(bands_object)
}

function decodeHtmlCharCodes(str) {
  return str.replace(/(&#(\d+);)/g, function(match, capture, charCode) {
    return String.fromCharCode(charCode);
  });
}

function populate_table(bands) {
    let band_table = document.getElementById('band-table');
    let i = 0;
    bands.forEach((band) => {
        let row = band_table.insertRow(i);
        let cell = row.insertCell(0);
        row.setAttribute('id', `band-${band.id}`);
        let bandName = band.bandname;
        let url = `/bands/${band.id}`;
        let link = `<a href='${url}'>${bandName}</a>`;

        cell.innerHTML = link;
        i++;
    });
}
