const onBlockClick = (event, block) => {
    // don't hijack nested anchor clicks
    if (event.target.tagName === 'A') {
        return;
    }

    event.preventDefault();
    const href = block.dataset.href;
    window.location = href;
};


const bindEvent = (node) => {
    node.addEventListener('click', (event) => {
        onBlockClick(event, node);
    });
};


const init = () => {
    const nodes = Array
            .from(document.querySelectorAll('.homepage-block'))
            .filter(node => !node.classList.contains('homepage-block--no-link'));
    nodes.map(bindEvent);
};

init();
