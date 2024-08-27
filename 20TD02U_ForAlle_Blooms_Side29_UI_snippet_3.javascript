// Hent elementer fra DOM
const addItemButton = document.getElementById('addItemButton');
const itemInput = document.getElementById('itemInput');
const itemList = document.getElementById('itemList');

// Legg til nytt element når knappen trykkes
addItemButton.addEventListener('click', function() {
    const itemText = itemInput.value.trim();
    
    if (itemText !== '') {
        const li = document.createElement('li');
        li.textContent = itemText;

        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Fjern';
        deleteButton.addEventListener('click', function() {
            itemList.removeChild(li);
        });

        li.appendChild(deleteButton);
        itemList.appendChild(li);

        itemInput.value = '';
    }
});