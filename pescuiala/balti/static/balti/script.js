removeChecked = () => {
    const filters = document.getElementsByClassName('filter-judete');
    console.log(filters);

    for (let i = 0; i < filters.length; i++) {
        filters[i].checked = false;
    }
}