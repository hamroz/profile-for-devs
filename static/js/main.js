// Get Search Form and Page Links
let searchForm = document.getElementById("searchForm");
let pageLinks = document.getElementsByClassName("page-link");

// Ensure Search form exists
if (searchForm) {
  for (let i = 0; pageLinks.length > i; i++) {
    pageLinks[i].addEventListener("click", function (e) {
      e.preventDefault();

      // Get the Data Attribute
      let page = this.dataset.page;

      // Add hidden search input to form
      searchForm.innerHTML += `<input value=${page} name="page" hidden/>`;

      // Submit Form
      searchForm.submit();
    });
  }
}
