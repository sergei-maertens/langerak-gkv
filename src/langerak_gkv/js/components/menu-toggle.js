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

    // profile search
    toggle('profile-list__search-icon', 'profile-list__search', 'opened');
    toggle('profile-list__search-close', 'profile-list__search', 'opened');
};

init();
