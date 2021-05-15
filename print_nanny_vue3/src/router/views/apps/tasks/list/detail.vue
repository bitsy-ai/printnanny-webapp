<template>
  <div class="card">
    <div class="card-body">
      <b-dropdown
        class="card-widgets"
        variant="black"
        toggle-tag="a"
        toggle-class="arrow-none p-0"
        right
      >
        <template v-slot:button-content>
          <i class="uil uil-ellipsis-h"></i>
        </template>

        <!-- item-->
        <a href="javascript:void(0);" class="dropdown-item">
          <i class="uil uil-file-upload mr-1"></i>Attachment
        </a>
        <!-- item-->
        <a href="javascript:void(0);" class="dropdown-item">
          <i class="uil uil-edit mr-1"></i>Edit
        </a>
        <!-- item-->
        <a href="javascript:void(0);" class="dropdown-item">
          <i class="uil uil-file-copy-alt mr-1"></i>Mark as Duplicate
        </a>
        <div class="dropdown-divider"></div>
        <!-- item-->
        <a href="javascript:void(0);" class="dropdown-item text-danger">
          <i class="uil uil-trash-alt mr-1"></i>Delete
        </a>
        <!-- end dropdown menu-->
      </b-dropdown>
      <div class="custom-control custom-checkbox float-left">
        <input id="completedCheck" type="checkbox" class="custom-control-input" />
        <label class="custom-control-label" for="completedCheck">Mark as completed</label>
      </div>
      <hr class="mt-4 mb-2" />
      <div class="row">
        <div class="col">
          <h4>Draft the new contract document for sales team</h4>

          <div class="row">
            <div class="col-6">
              <!-- assignee -->
              <p class="mt-2 mb-1 text-muted">Assigned To</p>
              <div class="media">
                <img
                  src="@assets/images/users/avatar-9.jpg"
                  alt="Arya S"
                  class="rounded-circle mr-2"
                  height="24"
                />
                <div class="media-body">
                  <h5 class="mt-1 font-14">Arya Stark</h5>
                </div>
              </div>
              <!-- end assignee -->
            </div>
            <!-- end col -->

            <div class="col-6">
              <!-- start due date -->
              <p class="mt-2 mb-1 text-muted">Due Date</p>
              <div class="media">
                <i class="uil uil-schedule font-18 text-success mr-1"></i>
                <div class="media-body">
                  <h5 class="mt-1 font-14">Today 10am</h5>
                </div>
              </div>
              <!-- end due date -->
            </div>
            <!-- end col -->
          </div>
          <!-- end row -->

          <!-- task description -->
          <div class="row mt-3">
            <div class="col">
              <div id="taskDesk">
                <p>This is a task description with markup support</p>
                <ul>
                  <li>Select a text to reveal the toolbar.</li>
                  <li>Edit rich document on-the-fly, so elastic!</li>
                </ul>
                <p>End of air-mode area</p>
              </div>
            </div>
            <!-- end col -->
          </div>
          <!-- end task description -->

          <!-- start sub tasks/checklists -->
          <h5 class="mt-4 mb-2 font-16">Checklists/Sub-tasks</h5>
          <div class="custom-control custom-checkbox mt-1">
            <input id="checklist1" type="checkbox" class="custom-control-input" />
            <label
              class="custom-control-label strikethrough"
              for="checklist1"
            >Find out the old contract documents</label>
          </div>

          <div class="custom-control custom-checkbox mt-1">
            <input id="checklist2" type="checkbox" class="custom-control-input" />
            <label
              class="custom-control-label strikethrough"
              for="checklist2"
            >Organize meeting sales associates to understand need in detail</label>
          </div>

          <div class="custom-control custom-checkbox mt-1">
            <input id="checklist3" type="checkbox" class="custom-control-input" />
            <label
              class="custom-control-label strikethrough"
              for="checklist3"
            >Make sure to cover every small details</label>
          </div>
          <!-- end sub tasks/checklists -->

          <!-- start attachments -->
          <h5 class="mt-4 mb-2 font-16">Attachments</h5>
          <div class="card mb-2 shadow-none border">
            <div class="p-1">
              <div class="row align-items-center">
                <div class="col-auto">
                  <div class="avatar-sm">
                    <span class="avatar-title rounded">.ZIP</span>
                  </div>
                </div>
                <div class="col pl-0">
                  <a href="javascript:void(0);" class="text-muted font-weight-bold">sales-assets.zip</a>
                  <p class="mb-0">2.3 MB</p>
                </div>
                <div class="col-auto">
                  <!-- Button -->
                  <a
                    v-b-tooltip.hover.bottom
                    href="javascript:void(0);"
                    title="Download"
                    class="btn btn-link text-muted btn-lg p-0"
                  >
                    <i class="uil uil-cloud-download"></i>
                  </a>
                  <a
                    v-b-tooltip.hover.bottom
                    href="javascript:void(0);"
                    title="Delete"
                    class="btn btn-link text-danger btn-lg p-0"
                  >
                    <i class="uil uil-multiply"></i>
                  </a>
                </div>
              </div>
            </div>
          </div>
          <div class="card mb-2 shadow-none border">
            <div class="p-1">
              <div class="row align-items-center">
                <div class="col-auto">
                  <img
                    src="@assets/images/projects/project-1.jpg"
                    class="avatar-sm rounded"
                    alt="file-image"
                  />
                </div>
                <div class="col pl-0">
                  <a
                    href="javascript:void(0);"
                    class="text-muted font-weight-bold"
                  >new-contarcts.docx</a>
                  <p class="mb-0">1.25 MB</p>
                </div>
                <div class="col-auto">
                  <!-- Button -->
                  <a
                    v-b-tooltip.hover.bottom
                    href="javascript:void(0);"
                    title="Download"
                    class="btn btn-link text-muted btn-lg p-0"
                  >
                    <i class="uil uil-cloud-download"></i>
                  </a>
                  <a
                    v-b-tooltip.hover.bottom
                    href="javascript:void(0);"
                    title="Delete"
                    class="btn btn-link text-danger btn-lg p-0"
                  >
                    <i class="uil uil-multiply"></i>
                  </a>
                </div>
              </div>
            </div>
          </div>
          <!-- end attachments -->

          <!-- comments -->
          <div class="row mt-3">
            <div class="col">
              <h5 class="mb-2 font-16">Comments</h5>

              <div class="media mt-3 p-1">
                <img
                  src="@assets/images/users/avatar-9.jpg"
                  class="mr-2 rounded-circle"
                  height="36"
                  alt="Arya Stark"
                />
                <div class="media-body">
                  <h5 class="mt-0 mb-0">
                    <span class="float-right text-muted font-12">4:30am</span>
                    Arya Stark
                  </h5>
                  <p
                    class="mt-1 mb-0 text-muted"
                  >Should I review the last 3 years legal documents as well?</p>
                </div>
              </div>
              <!-- end comment -->

              <hr />

              <div class="media mt-2 p-1">
                <img
                  src="@assets/images/users/avatar-5.jpg"
                  class="mr-2 rounded-circle"
                  height="36"
                  alt="Dominc B"
                />
                <div class="media-body">
                  <h5 class="mt-0 mb-0">
                    <span class="float-right text-muted font-12">3:30am</span>
                    Gary Somya
                  </h5>
                  <p
                    class="mt-1 mb-0 text-muted"
                  >@Arya FYI..I have created some general guidelines last year.</p>
                </div>
              </div>
              <!-- end comment-->

              <hr />
            </div>
            <!-- end col -->
          </div>
          <!-- end row -->

          <div class="row mt-2">
            <div class="col">
              <div class="border rounded">
                <form action="#" class="comment-area-box">
                  <textarea
                    rows="3"
                    class="form-control border-0 resize-none"
                    placeholder="Your comment..."
                  ></textarea>
                  <div class="p-2 bg-light">
                    <div class="float-right">
                      <button type="submit" class="btn btn-sm btn-success">
                        <i class="uil uil-message mr-1"></i>Submit
                      </button>
                    </div>
                    <div>
                      <a href="#" class="btn btn-sm px-1 btn-light">
                        <i class="uil uil-cloud-upload"></i>
                      </a>
                      <a href="#" class="btn btn-sm px-1 btn-light">
                        <i class="uil uil-at"></i>
                      </a>
                    </div>
                  </div>
                </form>
              </div>
              <!-- end .border-->
            </div>
            <!-- end col-->
          </div>
          <!-- end row-->
          <!-- end comments -->
        </div>
        <!-- end col -->
      </div>
    </div>
  </div>
  <!-- end row-->
</template>