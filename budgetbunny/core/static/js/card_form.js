document.getElementById("add-form").addEventListener("click", function () {
    const formContainer = document.getElementById("form-containers");
    const totalForms = document.getElementById("id_form-TOTAL_FORMS");

    const newIndex = totalForms.value;
    const emptyForm = formContainer[0].outerHTML.replace(/form-0/g, `form-${newIndex}`);

    formContainer.insertAdjacentHTML("beforeend", emptyForm);
    totalForms.value = parseInt(totalForms.value) + 1;

})