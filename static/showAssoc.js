$(document).ready(function() {
  $.get( "/getData/AA_courses.csv", function( data ) { initCourseData( data, "course-table", edit=false ) });
  $.get( "/getData/AA_certs.csv", function( data ) { initCertData( data, "cert-table", edit=false ) });
  $.get( "/getData/AA_assoc.csv", function( data ) { initAssocData( data, "assoc-table", edit=false ) });

  $("#download-pdf").click( function() {
    var title = $("#root-choice").val();
    assocTable.download("pdf", "Global Knowledge report", {
      orientation: "portrait", //set page orientation to portrait
      title: title //add title to report
    });
  });

  /* TAB NAV */

  $('#nav-tab a').on('click', function (e) {
    e.preventDefault();
    $(this).tab('show');
  });

  $('#nav-tab a').on('shown.bs.tab', function (e) {
    refreshTables();
  });

});