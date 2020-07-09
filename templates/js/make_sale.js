let albums;
let album_sale_hash;
let sale_hash = {};
let line_item_count = 1;

function load_function(albums_object, album_sale_hash_object) {
    albums_object = decodeHtmlCharCodes(albums_object);
    album_sale_hash_object = decodeHtmlCharCodes(album_sale_hash_object);
    albums = JSON.parse(albums_object);
    album_sale_hash = JSON.parse(album_sale_hash_object);
    hashify_sale_hash();
}

function decodeHtmlCharCodes(str) {
  return str.replace(/(&#(\d+);)/g, function(match, capture, charCode) {
    return String.fromCharCode(charCode);
  });
}

function hashify_sale_hash() {
    album_sale_hash.forEach((ash) => {
        sale_hash[ash['albumname']] = ash['price'];
    });
}

function display_line_item() {
    let sales_table = document.getElementById('sales-table');
    let row = sales_table.insertRow(line_item_count);
    row.id = `row-${line_item_count}`;
    ['album', 'quantity', 'price', 'add'].forEach((cell, i) => {
        let new_cell = row.insertCell(i);
        new_cell.id = `${cell}-${line_item_count}`;
        new_cell.className = `${cell}-cell`;
    });
    let album_cell = document.getElementById(`album-${line_item_count}`);
    let quantity_cell = document.getElementById(`quantity-${line_item_count}`);
    let price_cell = document.getElementById(`price-${line_item_count}`);
    let add_cell = document.getElementById(`add-${line_item_count}`);

    let select = document.createElement('select');
    select.id = `album-select-${line_item_count}`;
    select.className = 'album-select';
    select.setAttribute('onchange', `line_item_total(${line_item_count})`);
    populateSelect(select);

    let quantity = document.createElement('input');
    quantity.type = 'number';
    quantity.value = 1;
    quantity.id = `quantity-input-${line_item_count}`;
    quantity.className = 'quantity-input';
    quantity.setAttribute('onchange', `line_item_total(${line_item_count})`);

    let price = document.createElement('span');
    price.id = `line-item-price-${line_item_count}`;
    price.className = 'line-item-price';

    let add_button = document.createElement('button');
    add_button.className = 'add-line-item';
    add_button.onclick = new_line_item;
    add_button.innerText = 'Add';

    album_cell.insertAdjacentElement('afterbegin', select);
    quantity_cell.insertAdjacentElement('afterbegin', quantity);
    price_cell.insertAdjacentElement('afterbegin', price);
    add_cell.insertAdjacentElement('afterbegin', add_button);

    line_item_total(line_item_count);
    calculate_total();
}

function new_line_item() {
    line_item_count += 1;
    display_line_item();
}

function populateSelect(select) {
    albums.forEach((album) => {
        let option = document.createElement('option');
        option.id = album['id'];
        option.text = album['albumname'];
        select.add(option);
    });
}

function line_item_total(row) {
    let quantity = document.getElementById(`quantity-input-${row}`).value;
    let album = document.getElementById(`album-select-${row}`).value;
    let album_price = sale_hash[album].split('$')[1];
    let line_item_total = album_price * quantity;
    document.getElementById(
        `line-item-price-${row}`
    ).innerText = line_item_total.toFixed(2);
    calculate_total();
}

function calculate_total() {
    let total = 0;
    let iter = 1;
    while (iter <= line_item_count) {
        let li_price = parseFloat(
            document.getElementById(`line-item-price-${iter}`).innerText
        );
        total += li_price;
        iter++;
    }
    let total_cell = document.getElementById('sale-total');
    total = total.toFixed(2);
    total = `<b>$${total}</b>`;
    total_cell.innerHTML = total;
}

function prepare_submission() {
    let iter = 1;
    let albums = [];
    while (iter <= line_item_count) {
        let selected_option = document.getElementById(`album-select-${iter}`).selectedOptions;
        let album_id = selected_option[0].id;
        let quantity = document.getElementById(`quantity-input-${iter}`);
        quantity = parseInt(quantity.value);
        let album_hash = {'album_id': album_id};
        for (let i = 0; i < quantity; i++) {
            albums.push(album_hash);
        }
        iter++;
    }
    let post_object = {'line_items': albums};
    return post_object;
}

function submit() {
    let data = prepare_submission();
    let url = '/api/v1/resources/make_sale';

    fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(res => {
       console.log('Request Complete: ', res);
    });
    window.location.replace("/sales");
}