let sales;

function load_function(sales_object) {
    sales_object = decodeHtmlCharCodes(sales_object);
    sales = JSON.parse(sales_object);
}

function decodeHtmlCharCodes(str) {
  return str.replace(/(&#(\d+);)/g, function(match, capture, charCode) {
    return String.fromCharCode(charCode);
  });
}

function populate_table(sales) {
    let sales_table = document.getElementById('sales-table');
    let headers = sales_table.insertRow(0);
    headers.insertCell(0).innerHTML = 'Date of Sale';
    headers.insertCell(1).innerHTML = 'Albums';
    headers.insertCell(2).innerHTML = 'Price';

    sales.forEach((sale) => {
        let line_items = sale['line_items'];
        let li_html = '<ul>';
        let price_html = '<ul>';
        let total = 0;
        line_items.forEach((li) => {
           total += to_float(li['price']);
           li_html += `<li>${li['album_name']}</li>`;
           price_html += `<li>${li['price']}</li>`;
        });
        li_html += '</ul>';
        price_html += `<li><b>Total: ${total.toFixed(2)}</b></li>`;
        price_html += '</ul>';

        let row = sales_table.insertRow();
        let date_cell = row.insertCell(0);
        let album_cell = row.insertCell(1);
        let price_cell = row.insertCell(2);

        date_cell.setAttribute('class', 'date-cell');
        album_cell.setAttribute('class', 'album-cell');
        price_cell.setAttribute('class', 'price-cell');

        date_cell.innerHTML = `<b>${sale['date']}</b>`;
        album_cell.innerHTML = li_html;
        price_cell.innerHTML = price_html;
    });
}

function to_float(currency) {
    return parseFloat(currency.replace(/[$,]+/g, ''))
}