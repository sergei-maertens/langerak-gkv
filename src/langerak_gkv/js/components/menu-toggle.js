const toggle = (control, target, modifier, callback) => {
    const controlNode = document.querySelector(`.${control}`);
    if (!controlNode) {
        return;
    }
    const targetNode = document.querySelector(`.${target}`);
    const toggleClass = `${target}--${modifier}`;

    controlNode.addEventListener('click', () => {
        targetNode.classList.toggle(toggleClass);
        callback && callback(targetNode);
    });
};

const init = () => {
    toggle('menu__search', 'search-form', 'visible');
};

const scrollIntoView = (targetNode) => {
    targetNode.scrollIntoView({'behavior': 'smooth'});
};

init();
