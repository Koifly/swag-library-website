function toggle_expand(buttonId) {
  // Get the button that triggered this
  var theButton = document.getElementById(buttonId);

  // Remove border from expanded row
  document.getElementById("row_" + buttonId).classList.add("expanded-row");
  document.getElementById("row_" + buttonId).classList.remove("collapsed-row");

  // Change icon
  document.getElementById("icon_" + buttonId).classList.add("fa-angle-down");
  document.getElementById("icon_" + buttonId).classList.remove("fa-angle-up");
  theButton.setAttribute("expanded", "true");
}

function toggle_collapse(buttonId) {
  // Get the button that triggered this
  var theButton = document.getElementById(buttonId);
  
  // Add border to collapsed row
  document.getElementById("row_" + buttonId).classList.add("collapsed-row");
  document.getElementById("row_" + buttonId).classList.remove("expanded-row");

  // Change icon
  document.getElementById("icon_" + buttonId).classList.add("fa-angle-up");
  document.getElementById("icon_" + buttonId).classList.remove("fa-angle-down");
  theButton.setAttribute("expanded", "false");
}

function toggle_book(buttonId) {
  // Get the button that triggered this
  var theButton = document.getElementById(buttonId);

  if (theButton.getAttribute("expanded") == "false") {
    // Show info
    document.getElementById("blurb_" + buttonId).classList.add("show-info");
    document.getElementById("blurb_" + buttonId).classList.remove("hidden-info");
    document.getElementById("tags_" + buttonId).classList.add("show-info");
    document.getElementById("tags_" + buttonId).classList.remove("hidden-info");
    document.getElementById("actions_" + buttonId).classList.add("show-info");
    document.getElementById("actions_" + buttonId).classList.remove("hidden-info");
    theButton.setAttribute("expanded", "true");

    toggle_expand(buttonId)
  } else {
    // Hide info
    document.getElementById("blurb_" + buttonId).classList.add("hidden-info");
    document.getElementById("blurb_" + buttonId).classList.remove("show-info");
    document.getElementById("tags_" + buttonId).classList.add("hidden-info");
    document.getElementById("tags_" + buttonId).classList.remove("show-info");
    document.getElementById("actions_" + buttonId).classList.add("hidden-info");
    document.getElementById("actions_" + buttonId).classList.remove("show-info");

    toggle_collapse(buttonId)
  }
}

function toggle_series(buttonId) {
  // Get the button that triggered this
  var theButton = document.getElementById(buttonId);

  if (theButton.getAttribute("expanded") == "false") {
    // Show info
    document.getElementById("books_" + buttonId).classList.add("show-info");
    document.getElementById("books_" + buttonId).classList.remove("hidden-info");

    toggle_expand(buttonId)
    theButton.setAttribute("expanded", "true");
  } else {
    // Hide info
    document.getElementById("books_" + buttonId).classList.add("hidden-info");
    document.getElementById("books_" + buttonId).classList.remove("show-info");

    toggle_collapse(buttonId)
  }
}