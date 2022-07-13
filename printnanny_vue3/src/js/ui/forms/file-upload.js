/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: Chat
 */
import FileUpload from '../../components/file-upload';

class FileUploadForm {
  constructor() {

  }

  init() {
    new FileUpload().init();

  }
}

// init the dashboard
new FileUploadForm().init();
