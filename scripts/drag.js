import { Sortable } from '@shopify/draggable'

document.addEventListener('DOMContentLoaded', () => {
    console.log('DOMContentLoaded event fired');
    console.log('Draggable:', window.Draggable);
    const sortable = new Sortable(document.querySelectorAll('ul'), {
        draggable: 'p',
    });
    sortable.on('drag:start', (evt) => {
        // console.log('START')
        // console.log(evt)
        evt.data.source.classList.add('draggable--is-dragging');
    });

    sortable.on('drag:stop', (evt) => {
        console.log('STOP')
        console.log(evt)
        evt.data.source.classList.remove('draggable--is-dragging');
    });

    sortable.on('sortable:sort', (evt) => {
        // console.log('SORT')
        // console.log(evt)
        evt.data.dragEvent.source.classList.add('draggable--is-over');
    });

    sortable.on('sortable:sorted', (evt) => {
        console.log('SORTED')
        console.log(evt)
        evt.data.dragEvent.source.classList.remove('draggable--is-over');
    });
    }
);

