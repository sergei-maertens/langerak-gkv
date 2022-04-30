const SELECTOR = '.scroll-into-view';

const scrollIntoView = () => {
    // we can only scroll the first node matching the selector into view
    const node = document.querySelector(SELECTOR);
    if (!node) return;
    node.scrollIntoView({behavior: 'smooth'});
    if (node.classList.contains('scroll-into-view--focus')) {
        node.focus();
    }
};

document.addEventListener('DOMContentLoaded', scrollIntoView);
