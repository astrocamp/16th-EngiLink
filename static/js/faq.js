let elements = document.querySelectorAll("[data-menu]");
for (let i = 0; i < elements.length; i++) {
    let main = elements[i];

    main.addEventListener("click", function () {
        let element = main.parentElement;
        let indicators = main.querySelectorAll("img");
        let child = element.querySelector("#menu");
        let h = main.querySelector("p");

        h.classList.toggle("font-semibold");
        child.classList.toggle("hidden");
        indicators[0].classList.toggle("rotate-180");
    });
    main.parentElement.addEventListener("click", function (event) {
        if (event.target !== main) {
            main.click();
        }
    });
}