const getBands = async () => {
    const response = await fetch('http://localhost:5000/api/v1/resources/bands');
    const returnJson = await response.json();
    return returnJson;
};

let allBands = getBands();
allBands.then(function(results) {
    let band_table = document.getElementById('band-table');

    results.forEach((band) => {
        let row = band_table.insertRow(band.id);
        let cell = row.insertCell(0);
        row.setAttribute('id', `band-${band.id}`);
        let bandName = band.bandname;
        let url = `/bands/${band.id}`;
        let link = `<a href='${url}'>${bandName}</a>`;

        cell.innerHTML = link;
    });
});