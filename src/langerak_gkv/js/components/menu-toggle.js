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
    toggle('menu__profile', 'user-actions', 'visible', openLoginModal);
    toggle('menu__search', 'search-form', 'visible');

    // profile search
    toggle('profile-list__search-icon', 'profile-list__search', 'opened');
    toggle('profile-list__search-close', 'profile-list__search', 'opened');
};

const openLoginModal = (targetNode) => {
    const isVisible = targetNode.classList.contains('user-actions--visible');
    if (!isVisible) return;

    const loginLink = targetNode.querySelector('[data-modal="login"]');
    loginLink && loginLink.click();
};

init();
