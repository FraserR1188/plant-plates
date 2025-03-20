document.addEventListener("DOMContentLoaded", function () {
  let sidenav = document.querySelectorAll(".sidenav");
  M.Sidenav.init(sidenav);
});

document.addEventListener("DOMContentLoaded", function () {
  var elems = document.querySelectorAll(".modal");
  M.Modal.init(elems);
});

document.addEventListener("DOMContentLoaded", function () {
  var elems = document.querySelectorAll(".parallax");
  M.Parallax.init(elems);
});

document.addEventListener("DOMContentLoaded", function () {
  var elems = document.querySelectorAll(".sidenav");
  var instances = M.Sidenav.init(elems);
});

document.addEventListener("DOMContentLoaded", function () {
  var modalElem = document.getElementById("login-success-modal");
  var modalInstance = M.Modal.init(modalElem);
  modalInstance.open();
  setTimeout(function () {
    modalInstance.close();
  }, 2000);
});

document.addEventListener("DOMContentLoaded", function () {
  // Check if the URL has the query parameter logout=true
  const urlParams = new URLSearchParams(window.location.search);
  if (urlParams.get("logout") === "true") {
    var modalElem = document.getElementById("logout-success-modal");
    var modalInstance = M.Modal.init(modalElem);
    modalInstance.open();
    setTimeout(function () {
      modalInstance.close();
      // Optionally, remove the query parameter from the URL after closing
      window.history.replaceState({}, document.title, window.location.pathname);
    }, 2000);
  }
});

document.addEventListener("DOMContentLoaded", function () {
  var elems = document.querySelectorAll("select");
  M.FormSelect.init(elems);
});

document.addEventListener("DOMContentLoaded", function () {
  // Initialize modal(s)
  var elems = document.querySelectorAll(".modal");
  var instances = M.Modal.init(elems);

  // Attach event listener to delete buttons
  const deleteButtons = document.querySelectorAll(".delete-btn");
  deleteButtons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      // Retrieve category id and name from data attributes
      var categoryId = btn.getAttribute("data-category-id");
      var categoryName = btn.getAttribute("data-category-name");

      // Update the modal message
      document.getElementById("deleteMessage").textContent =
        "Are you sure you want to delete the category '" +
        categoryName +
        "'? This action will delete all recipes in this category.";

      // Dynamically update the form action URL
      // The placeholder '__placeholder__' will be replaced with the actual categoryId.
      var deleteUrl =
        "{{ url_for('delete_category', category_id='__placeholder__') }}".replace(
          "__placeholder__",
          categoryId
        );
      document.getElementById("deleteForm").action = deleteUrl;
    });
  });
});
