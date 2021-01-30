class Menu {
    constructor(root) {
        this.root = root;
        this.hamberder = root.querySelector('.menu__hamberder');
        this.bindEvents();
    }

    bindEvents() {
        this.hamberder.addEventListener('click', () => {
            this.root.classList.toggle('menu--opened');
        });
    }
}


const init = () => {
    const menuNodes = document.querySelectorAll('.menu');
    Array.from(menuNodes).forEach(node => new Menu(node));
};


init();
