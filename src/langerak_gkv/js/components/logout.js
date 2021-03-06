
const logOut = (event) => {
    event.preventDefault();
    const form = document.querySelector('.logout-form');
    form.submit();
};


const init = () => {
    const logoutLinks = document.querySelectorAll('.logout-url');
    Array.from(logoutLinks).forEach(link => link.addEventListener('click', logOut));
};


init();
