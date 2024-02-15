function toggle(buttonId) {
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

    // Remove border from expanded row
    document.getElementById("row_" + buttonId).classList.add("expanded-row");
    document.getElementById("row_" + buttonId).classList.remove("collapsed-row");

    // Change icon
    document.getElementById("icon_" + buttonId).classList.add("fa-angle-down");
    document.getElementById("icon_" + buttonId).classList.remove("fa-angle-up");
    theButton.setAttribute("expanded", "true");
  } else {
    // Hide info
    document.getElementById("blurb_" + buttonId).classList.add("hidden-info");
    document.getElementById("blurb_" + buttonId).classList.remove("show-info");
    document.getElementById("tags_" + buttonId).classList.add("hidden-info");
    document.getElementById("tags_" + buttonId).classList.remove("show-info");
    document.getElementById("actions_" + buttonId).classList.add("hidden-info");
    document.getElementById("actions_" + buttonId).classList.remove("show-info");

    // Add border to collapsed row
    document.getElementById("row_" + buttonId).classList.add("collapsed-row");
    document.getElementById("row_" + buttonId).classList.remove("expanded-row");

    // Change icon
    document.getElementById("icon_" + buttonId).classList.add("fa-angle-up");
    document.getElementById("icon_" + buttonId).classList.remove("fa-angle-down");
    theButton.setAttribute("expanded", "false");
  }
}