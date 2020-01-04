const toggle = (control, target, modifier) => {
    const controlNode = document.querySelector(`.${control}`);
    const targetNode = document.querySelector(`.${target}`);
    const toggleClass = `${target}--${modifier}`;

    controlNode.addEventListener('click', () => {
        targetNode.classList.toggle(toggleClass);
    });
};

const init = () => {
    toggle('menu__profile', 'user-actions', 'visible');
    toggle('menu__search', 'search-form', 'visible');
};

init();
