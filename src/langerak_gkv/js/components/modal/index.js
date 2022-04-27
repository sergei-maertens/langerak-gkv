
class Modal {
    constructor(node, triggerNodes) {
        this.node = node;
        this.triggerNodes = triggerNodes;
        this.setupEvents();

        this._contentLoaded = false;
    }

    static initialize() {
        const triggerNodes = document.querySelectorAll('.modal-trigger');
        const modalNodes = document.querySelectorAll('.modal');

        let nodesByType = {};
        let triggersByType = {};

        Array.from(modalNodes).forEach(node => {
            if (node.dataset.modal) {
                nodesByType[node.dataset.modal] = node;
            }
        });

        Array.from(triggerNodes).forEach(node => {
            if (node.dataset.modal) {
                if (!triggersByType[node.dataset.modal]) triggersByType[node.dataset.modal] = [];
                triggersByType[node.dataset.modal].push(node);
            }
        });

        // initialize the instances
        for (const modalType of Object.keys(nodesByType)) {
            // can't activate a modal if there's no trigger
            if (!triggersByType[modalType] || !triggersByType[modalType].length) {
                continue;
            }
            new this(nodesByType[modalType], triggersByType[modalType]);
        }
    }

    setupEvents() {
        // open modal
        this.triggerNodes.forEach(triggerNode => {
            triggerNode.addEventListener('click', event => {
                event.preventDefault();

                this.node.classList.remove('modal--inactive');
                const dataLoadUrl = triggerNode.dataset.modalLoad;
                if (!dataLoadUrl || this._contentLoaded) return;

                const contentContainer = this.node.querySelector('.modal__content');

                window.fetch(dataLoadUrl)
                    .then(response => response.text())
                    .then(html => {
                        contentContainer.insertAdjacentHTML('beforeend', html);
                        this._contentLoaded = true;
                    });
            });
        });

        this.node.querySelector('.modal__close').addEventListener('click', () => {
            this.node.classList.add('modal--inactive');
        });
    }
}


Modal.initialize();
