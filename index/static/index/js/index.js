(function () {
  'use strict';

  const content = document.getElementById('content');
  const style = document.getElementById('style');
  const placeholders = document.querySelectorAll('.placeholder');
  const labels = document.querySelectorAll('label');
  const btn = document.querySelector('button');
  const form = document.querySelector('form');
  const mainForm = document.querySelector('.main-form');
  const loadingScreen = document.querySelector('.loading-screen');

  labels[0].innerHTML = 'Upload content image';
  labels[1].innerHTML = 'Upload style image';

  content.addEventListener('change', previewContent, false);
  style.addEventListener('change', previewStyle, false);
  btn.addEventListener('click', function() {
    mainForm.classList.add('hidden');
    btn.classList.add('hidden');
    loadingScreen.classList.remove('hidden');
    form.submit();
  });

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