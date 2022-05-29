$(document).on('click', '[data-toggle="lightbox"]', function(event) {
    event.preventDefault();
    $(this).ekkoLightbox();
    $(this).ekkolightbox({
    loadingMessage: "Loading…",
    showArrows: true,
    leftArrow: "<<<",
    rightArrow: ">>>"
  });
  });