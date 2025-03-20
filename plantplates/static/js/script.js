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
