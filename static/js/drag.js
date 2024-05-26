import { Sortable } from '@shopify/draggable';
import Alpine from 'alpinejs';

function dragElement(element){
    const sortable = new Sortable(document.querySelectorAll('ul'), {
        draggable: 'li',
        animation: 150,
    });

    sortable.on('drag:start', (evt) => {
        evt.data.source.classList.add('draggable--is-dragging');
    });

    sortable.on('sortable:sorted', (evt) => {
        evt.data.dragEvent.source.classList.remove('draggable--is-over');
        sendPositionUpdate(evt.data.dragEvent.source.parentElement);
    });
}


function sendPositionUpdate(list) {
    const items = Array.from(list.children);
    const positions = items.map((item, index) => {
        const id = item.dataset.id;
        return { id: parseInt(id), position: index + 1 }; 
    });


    fetch('/resumes/update_positions/', {
        method: 'POST',
        headers: {
            'Content-Type': "application/json",
            'X-CSRFToken': getCsrfToken(),
        },
        body: JSON.stringify({ positions: positions }),
    }).then(response => {
        return response.json();
    })
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


document.addEventListener('alpine:init', () => {
    Alpine.data('draggable', () => ({
        init(){
            dragElement();
        }
    }))
})
