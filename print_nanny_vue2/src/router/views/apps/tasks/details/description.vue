<template>
  <div class="card d-block">
    <div class="card-body">
      <b-dropdown
        right
        variant="white"
        class="card-widgets"
        toggle-class="arrow-none p-0"
        toggle-tag="a"
      >
        <template slot="button-content">
          <i class="uil uil-ellipsis-h"></i>
        </template>
        <b-dropdown-item href="javascript: void(0);">
          <i class="uil uil-file-upload mr-1"></i>Attachment
        </b-dropdown-item>
        <b-dropdown-item href="javascript: void(0);">
          <i class="uil uil-edit mr-1"></i>Edit
        </b-dropdown-item>
        <b-dropdown-item href="javascript: void(0);">
          <i class="uil uil-file-copy-alt mr-1"></i>Mark as Duplicate
        </b-dropdown-item>
        <b-dropdown-divider></b-dropdown-divider>
        <b-dropdown-item href="javascript: void(0);" variant="danger">
          <i class="uil uil-trash-alt mr-1"></i>Delete
        </b-dropdown-item>
      </b-dropdown>
      <!-- end dropdown-->

      <b-form-checkbox id="checkbox-1" class="float-left">Mark as completed</b-form-checkbox>
      <!-- end custom-checkbox-->

      <div class="clearfix"></div>

      <h3 class="mt-3">Draft the new contract document for sales team</h3>

      <div class="row">
        <div class="col-6">
          <!-- assignee -->
          <p class="mt-2 mb-1 text-muted font-weight-bold font-12 text-uppercase">Assigned To</p>
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
          <p class="mt-2 mb-1 text-muted font-weight-bold font-12 text-uppercase">Due Date</p>
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

      <h5 class="mt-3">Overview:</h5>

      <p
        class="text-muted mb-4"
      >This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer. Some quick example text to build on the card title and make up the bulk of the card's content. Some quick example text to build on the card title and make up.</p>

      <!-- start sub tasks/checklists -->
      <h5 class="mt-4 mb-2 font-16">Checklists/Sub-tasks</h5>

      <b-form-checkbox id="checklist1" class="mt-1">Find out the old contract documents</b-form-checkbox>
      <b-form-checkbox
        id="checklist2"
        class="mt-1"
      >Organize meeting sales associates to understand need in detail</b-form-checkbox>

      <b-form-checkbox id="checklist3" class="mt-1">Make sure to cover every small details</b-form-checkbox>
      <!-- end sub tasks/checklists -->
    </div>
    <!-- end card-body-->
  </div>
  <!-- end card-->
</template>