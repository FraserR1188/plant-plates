document.addEventListener("DOMContentLoaded", function () {
  // Initialize sidenav
  let sidenavElems = document.querySelectorAll(".sidenav");
  M.Sidenav.init(sidenavElems);

  // Initialize modals
  let modalElems = document.querySelectorAll(".modal");
  let modalInstances = M.Modal.init(modalElems);

  // Open login modal immediately (if it exists)
  let loginModalElem = document.getElementById("login-success-modal");
  if (loginModalElem) {
    let loginModalInstance =
      M.Modal.getInstance(loginModalElem) || M.Modal.init(loginModalElem);
    loginModalInstance.open();
    setTimeout(() => loginModalInstance.close(), 2000);
  }

  // Check for logout query parameter to trigger logout modal
  const urlParams = new URLSearchParams(window.location.search);
  if (urlParams.get("logout") === "true") {
    let logoutModalElem = document.getElementById("logout-success-modal");
    if (logoutModalElem) {
      let logoutModalInstance =
        M.Modal.getInstance(logoutModalElem) || M.Modal.init(logoutModalElem);
      logoutModalInstance.open();
      setTimeout(() => {
        logoutModalInstance.close();
        window.history.replaceState(
          {},
          document.title,
          window.location.pathname
        );
      }, 2000);
    }
  }

  // Initialize parallax
  let parallaxElems = document.querySelectorAll(".parallax");
  M.Parallax.init(parallaxElems);

  // Initialize form select
  let selectElems = document.querySelectorAll("select");
  M.FormSelect.init(selectElems);

  // Attach event listener to delete buttons for dynamic modal updates
  const deleteButtons = document.querySelectorAll(".delete-btn");
  deleteButtons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var categoryId = btn.getAttribute("data-category-id");
      var categoryName = btn.getAttribute("data-category-name");
      document.getElementById("deleteMessage").textContent =
        "Are you sure you want to delete the category '" +
        categoryName +
        "'? This action will delete all recipes in this category.";
      var deleteUrl =
        "{{ url_for('delete_category', category_id='__placeholder__') }}".replace(
          "__placeholder__",
          categoryId
        );
      document.getElementById("deleteForm").action = deleteUrl;
    });
  });
});
