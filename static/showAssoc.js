$(document).ready(function() {
  editMode.set( false );

  $.get( "/getData/AA_courses.csv", function( data ) { initCourseData( data, "course-table" ) });
  $.get( "/getData/AA_certs.csv", function( data ) { initCertData( data, "cert-table" ) });
  $.get( "/getData/AA_assoc.csv", function( data ) { initAssocData( data, "assoc-table" ) });

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
    alert("hi")
    $(e.target)
      .addClass('text-primary')
      .removeClass('text-muted');
    refreshTables();
  });

  $('#nav-tab a').on('hidden.bs.tab', function (e) {
    $(e.target)
      .addClass('text-muted')
      .removeClass('text-primary');
    refreshTables();
  });

});