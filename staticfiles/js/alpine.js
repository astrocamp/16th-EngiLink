import Alpine from "alpinejs"

document.addEventListener('alpine:init', () => {
  Alpine.data('fileUpload', () => ({
      previewImage(event, previewId) {
          const file = event.target.files[0];
          if (file) {
              const reader = new FileReader();
              reader.onload = (e) => {
                  const previewContainer = document.getElementById(previewId + '_container');
                  const previewImage = document.getElementById(previewId);
                  previewImage.src = e.target.result;
                  previewContainer.classList.replace('hidden', 'block');
              };
              reader.readAsDataURL(file);
          }
      }
  }));
});


Alpine.start();


