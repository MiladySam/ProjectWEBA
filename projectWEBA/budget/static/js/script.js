(function () {
    document.querySelector('#categorieInput').addEventListener('keydown', function (e) {
        if (e.keyCode != 13) {
            return;
        }
        e.preventDefault();
        var categorieNom = this.value.trim();
        if (categorieNom == '') {
            document.getElementById('error').textContent = 'Veuillez saisir quelque chose.';
            return;
        }
        this.value = '';
        document.getElementById('error').textContent = ''; // Clear the error message
        ajouteNouvelleCat(categorieNom);
        updateCategoriesString();
        enleveCat();
    });

    function ajouteNouvelleCat(nom) {
        document.querySelector('#categoriesContainer').insertAdjacentHTML('beforeend',
            `<li class="categorie">
            <span class="name">${nom}</span>
            <span onclick="enleveCat(this)" class="btnEnleve  bold ">🗑️</span>
        </li>`);
    }




})();

function fetchCategorieArray() {
    var categories = [];
    document.querySelectorAll('.categorie').forEach(function (e) {
        var nom = e.querySelector('.name').innerHTML.trim();
        if (nom == '') return;
        categories.push(nom);
    });
    return categories;
}



function updateCategoriesString() {
    var categories = fetchCategorieArray();
    document.querySelector('input[name="categorieString"]').value = categories.join(',');
}


function enleveCat(e) {
    e.parentElement.remove();
    updateCategoriesString();
}


