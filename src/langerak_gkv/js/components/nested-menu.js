const ICON_CHANGES = {
    keyboard_arrow_down: 'keyboard_arrow_up',
    keyboard_arrow_up: 'keyboard_arrow_down',
};

const bindMobileClick = (node) => {
    const toggleNode = node.querySelector('.menu__nested-toggle');

    if (!toggleNode || toggleNode.classList.contains('menu__nested-toggle--desktop')) {
        return;
    }

    const nestedMenuNode = node.querySelector('.menu__nested-menu');
    const iconNode = toggleNode.querySelector('.material-icons');

    toggleNode.addEventListener('click', (event) => {
        event.preventDefault();
        const shouldBeShown = iconNode.innerText === 'keyboard_arrow_down';
        nestedMenuNode.classList.toggle('menu__nested-menu--opened', shouldBeShown);
        iconNode.innerText = ICON_CHANGES[iconNode.innerText];
    });
};


const bindHover = (node) => {
    if (node.classList.contains('menu__item--leaf')) {
        return;
    }

    const nestedMenuNode = node.querySelector('.menu__nested-menu');
    if (!nestedMenuNode) {
        return;
    }

    let scheduledClose;

    const clearScheduledClose = () => scheduledClose && window.clearTimeout(scheduledClose);

    const showNestedMenu = (event) => {


        nestedMenuNode.addEventListener('mouseleave', hideNestedMenu);
        nestedMenuNode.addEventListener('mouseenter', clearScheduledClose);
        if (nestedMenuNode.classList.contains('menu__nested-menu--opened')) {
            return;
        }
        nestedMenuNode.classList.add('menu__nested-menu--opened');
    };

    const hideNestedMenu = () => {
        scheduledClose = window.setTimeout(() => {
            nestedMenuNode.removeEventListener('mouseleave', hideNestedMenu);
            nestedMenuNode.removeEventListener('mouseenter', clearScheduledClose);
            nestedMenuNode.classList.remove('menu__nested-menu--opened');
        }, 100);
    };

    node.addEventListener('mouseenter', showNestedMenu);
    node.addEventListener('mouseleave', () => {
        scheduledClose = window.setTimeout(hideNestedMenu, 100);
    });
};


const init = () => {
    const nodes = document.querySelectorAll('.menu__item');
    nodes.forEach(bindMobileClick);
    nodes.forEach(bindHover);
};

init();
