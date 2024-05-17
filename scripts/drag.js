import { Sortable } from '@shopify/draggable'

document.addEventListener('DOMContentLoaded', () => {
    console.log('DOMContentLoaded event fired');
    console.log('Draggable:', window.Draggable);
    const sortable = new Sortable(document.querySelectorAll('ul'), {
        draggable: 'p',
    });
    sortable.on('drag:start', (evt) => {
        evt.data.source.classList.add('draggable--is-dragging');
    });

    sortable.on('drag:stop', (evt) => {
        evt.data.source.classList.remove('draggable--is-dragging');
    });

    sortable.on('sortable:sort', (evt) => {
        evt.data.dragEvent.source.classList.add('draggable--is-over');
    });

    sortable.on('sortable:sorted', (evt) => {
        evt.data.dragEvent.source.classList.remove('draggable--is-over');
        updateLocalStorage()
    });
    }
)



function updateLocalStorage(){
    const lists = document.querySelectorAll("ul")
    lists.forEach(list => {
        const id = list.id
        const childrenArray = Array.from(list.children)
        const items = Array.from(list.children).map(p => p.outerHTML)
        if (id && items.length > 0) {
            localStorage.setItem(id, JSON.stringify(items))
        }
        let storedItems = JSON.parse(localStorage.getItem(id)) || [];
        storedItems = storedItems.filter(item => !item.includes('draggable-mirror'))

        if (id && storedItems.length > 0) {
            localStorage.setItem(id, JSON.stringify(storedItems))
        }
    })

}

function populateList(items, itemsList){
    if (items.length > 0){
        itemsList.innerHTML = items.join('')
    }
}


document.addEventListener("DOMContentLoaded", () =>{
    const lists = document.querySelectorAll("ul")
    lists.forEach(list => {
        const id = list.id
        const storedItems = JSON.parse(localStorage.getItem(id)) || []
        populateList(storedItems, list)
    })
})

