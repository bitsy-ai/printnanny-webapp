/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: File-Upload
 */

import Dropzone from 'dropzone/dist/dropzone';

class FileUpload {

  constructor() {

  }

  init = function () {
    // Disable auto discovery

    Dropzone.autoDiscover = false;


    document.querySelectorAll('[data-plugin="dropzone"]').forEach(function (element){
      const actionUrl = element.action;

      const previewContainer = element.getAttribute('data-previews-container');

      const opts = { url: actionUrl };
      if (previewContainer) {
        opts['previewsContainer'] = previewContainer;
      }

      const uploadPreviewTemplate = element.getAttribute('data-upload-preview-template');
      if (uploadPreviewTemplate) {
        opts['previewTemplate'] = document.querySelector(uploadPreviewTemplate).innerHTML;
      }

      new Dropzone(element,opts);

    });

  }


}

export default FileUpload
