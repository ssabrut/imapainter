(function () {
  'use strict';

  const content = document.getElementById('content');
  const style = document.getElementById('style');
  const placeholders = document.querySelectorAll('.placeholder');

  content.addEventListener('change', previewContent, false);
  style.addEventListener('change', previewStyle, false);

  function previewContent(e) {
    if (window.FileReader) {
      const previewContent = document.getElementById('preview-content');
      const img = e.target.files[0];
      const reader = new FileReader();
      if (img && img.type.match('image.*')) {
        reader.readAsDataURL(img);
      }

      reader.onloadend = function () {
        previewContent.src = reader.result;
        placeholders[0].style.display = 'none';
      }
    }
  }

  function previewStyle(e) {
    if (window.FileReader) {
      const previewStyle = document.getElementById('preview-style');
      const img = e.target.files[0];
      const reader = new FileReader();
      if (img && img.type.match('image.*')) {
        reader.readAsDataURL(img);
      }

      reader.onloadend = function () {
        previewStyle.src = reader.result;
        placeholders[1].style.display = 'none';
      }
    }
  }
})();